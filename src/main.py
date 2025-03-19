# main.py - Entry point for the application

from services.api import start_api
from services.database import connect_to_db


def main():
    print("Starting the application...")
    connect_to_db()
    start_api()
    print("Application is running!")


if __name__ == "__main__":
    main()
