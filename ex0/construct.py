import sys
import site
import os


def construct():
    print("Constructing the project...")
    if sys.prefix != sys.base_prefix:
        print("\nMATRIX STATUS: Welcome to the construct")
        print("\nCurrent Python: ", sys.executable)
        print("Virtual Environment: ", os.path.basename(sys.prefix))
        print("Environment Path: ", sys.prefix)
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting "
              "\nthe global environment.")
        print("\nPackage installation path: ")
        paths = site.getsitepackages()
        if paths:
            print(paths[0])
    else:
        print("\nMATRIX STATUS: You're still plugged in")
        print("\nCurrent Python: ", sys.executable)
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_venv")
        print("source matrix_venv/bin/activate\t# On Unix")
        print("matrix_env\nScripts\nactivate\t# On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    try:
        construct()
    except Exception as e:
        print(f"An error occurred: {e}")
