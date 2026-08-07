import importlib


def validate_packages() -> bool:
    packages = [
        "pandas",
        "numpy",
        "matplotlib",
    ]

    print("Checking dependencies:")

    for package in packages:
        try:
            module = importlib.import_module(package)
            print(f"[OK] {package} ({module.__version__})")

        except ImportError:
            print(f"[KO] {package} missing")
            print("Install with: pip install -r requirements.txt")
            return False

    return True


def process_matrix() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    data = np.random.rand(1000)
    df = pd.DataFrame(data, columns=["matrix_data"])

    print("Generating visualization...")

    plt.plot(df["matrix_data"])
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def enter_the_matrix() -> None:
    print("LOADING STATUS: Loading programs...")

    if not validate_packages():
        return

    process_matrix()


if __name__ == "__main__":
    enter_the_matrix()
