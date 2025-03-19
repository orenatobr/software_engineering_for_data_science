# database.py - Handles database connections
import random
import time


def connect_to_db():
    """Simulates a database connection."""
    print("Connecting to the database...")
    time.sleep(1)
    if random.choice([True, False]):
        print("Database connected successfully!")
    else:
        raise Exception("Failed to connect to the database.")
