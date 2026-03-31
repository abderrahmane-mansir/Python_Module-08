import sys
import random

REQUIRED_LIBS = ["pandas", "requests", "matplotlib"]


def check_dependencies():
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    missing = []
    modules = {}

    for lib in REQUIRED_LIBS:
        try:
            # Dynamic import keeps dependency checks generic and reusable.
            module = __import__(lib)
            version = getattr(module, "__version__", "unknown")
            modules[lib] = module

            if lib == "pandas":
                msg = "Data manipulation ready"
            elif lib == "requests":
                msg = "Network access ready"
            elif lib == "matplotlib":
                msg = "Visualization ready"
            else:
                msg = "Ready"

            print(f"[OK] {lib} ({version}) - {msg}")

        except ImportError:
            print(f"[MISSING] {lib}")
            missing.append(lib)

    return missing, modules


def show_install_instructions(missing):
    print("\nMissing dependencies detected!")
    print("Install them with:")

    print("\npip:")
    print("pip install -r requirements.txt")

    print("\nPoetry:")
    print("poetry install")

    sys.exit(1)


def run_analysis(modules):
    # Use already-validated imports from check_dependencies.
    pandas = modules["pandas"]
    matplotlib = modules["matplotlib"]
    # Import pyplot explicitly from matplotlib so plotting APIs are available.
    plt = __import__(f"{matplotlib.__name__}.pyplot", fromlist=["pyplot"])

    print("\nAnalyzing Matrix data...")

    smooth_y = []
    value = random.uniform(40, 60)
    # Random walk: each point is a small change from the previous one
    # (smoother than pure noise).
    for _ in range(1000):
        value += random.uniform(-1.5, 1.5)
        smooth_y.append(value)

    data = pandas.DataFrame({
        "x": range(1000),
        "y": smooth_y
    })
    print("Processing 1000 data points...")

    plt.figure()
    plt.plot(data["x"], data["y"])

    print("Generating visualization...")

    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    missing, modules = check_dependencies()

    if missing:
        show_install_instructions(missing)

    run_analysis(modules)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting gracefully.")
        sys.exit(0)
