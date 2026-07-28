import sys

def check_matrix() -> None:
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again.")

    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Current Python: {sys.executable}")
        print(f"Environment Path: {sys.executable}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print("/path/to/matrix_env/lib/python3.11/site-packages")

if __name__ == "__main__ ":
    check_matrix()
