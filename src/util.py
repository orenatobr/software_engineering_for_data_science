# utils.py - Utility functions


def format_response(data):
    """Formats data into a standardized JSON response."""
    return {"status": "success", "data": data}


def validate_input(value, expected_type):
    """Validates if a value matches the expected type."""
    return isinstance(value, expected_type)


def retry_on_failure(func, retries=3):
    """Retries a function execution in case of failure."""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
    raise Exception("Function failed after retries")
