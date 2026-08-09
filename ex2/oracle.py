import os



def oracle() -> None:
    env_variables = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    try:
        from dotenv import load_dotenv
    except ImportError:
        print("Missing dependencies please use pip install -r requirements.txt")
    load_dotenv()
    mode = os.getenv("MATRIX_MODE")

    if mode == "development":
        print("Mode: development")

        for variable in env_variables:
            value = os.getenv(variable)

            if value is not None:
                if variable == "API_KEY":
                    print("API Access: Authenticated")
                else:
                    print(f"{variable}: {value}")
            else:
                print(f"Error: {variable} is missing")

    elif mode == "production":
        print("Mode: production")

        for variable in env_variables:
            value = os.getenv(variable)

            if value is not None:
                print(f"{variable}: configured")
            else:
                print(f"Error: {variable} is missing")

    else:
        print("Error: MATRIX_MODE must be present "
              "and be development or production")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix.\n")
    oracle()
