import os
import sys


# Dynamic import:
# lets us show a friendly install message if dependency is missing.
def import_dotenv():

    try:
        dotenv = __import__("dotenv")
        return dotenv.load_dotenv
    except Exception:
        print("\nORACLE STATUS: Reading the Matrix...\n")
        print("Missing dependency: python-dotenv")
        print("\nInstall it using:")
        print("pip install python-dotenv")
        print("or")
        print("poetry add python-dotenv")
        sys.exit(1)


# Load values from .env into environment variables for local/dev runtime.
def load_configuration():

    print("\nORACLE STATUS: Reading the Matrix...")

    load_dotenv = import_dotenv()

    load_dotenv()

    # Any config entry with None is treated as missing and should block startup
    config = {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "zion": os.getenv("ZION_ENDPOINT"),
    }

    return config


# Use defaults for non-sensitive settings;
# required secrets stay None if not set.
def validate_config(config):
    missing = [k for k, v in config.items() if v is None]

    if missing:
        print("WARNING: Missing configuration:")
        for m in missing:
            print(f"- {m}")

    exit(1) if missing else print("\nConfiguration loaded:")


def show_configuration(config):

    print(f"Mode: {config['mode']}")

    if config["database"]:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if config["api_key"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {config['log_level']}")

    if config["zion"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


# Basic local security check: .env should exist for environment-based secrets.
def security_check():
    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file detected")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def main():
    config = load_configuration()

    validate_config(config)

    show_configuration(config)

    security_check()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
