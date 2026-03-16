"""
Retry pattern for transient errors.
"""

import time


class TransientError(Exception):
    """Raised for temporary failures that can be retried."""


def flaky_task(attempt):
    """Fail for the first two attempts, then succeed."""
    if attempt < 3:
        raise TransientError(f"temporary failure at attempt {attempt}")
    return "success"


def run_with_retry(max_attempts=3, delay_seconds=0.1):
    for attempt in range(1, max_attempts + 1):
        try:
            return flaky_task(attempt)
        except TransientError as exc:
            if attempt == max_attempts:
                return f"Giving up: {exc}"
            time.sleep(delay_seconds)


if __name__ == "__main__":
    print("Result:", run_with_retry())
