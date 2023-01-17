import time


def rate_limit(calls_per_minute):
    # The time of the last call
    last_call_time = 0

    # The number of calls made in the current minute
    calls_in_current_minute = 0

    #set the running start_time
    start = None

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal last_call_time, calls_in_current_minute, start

            if start is None:
                start = time.time()

            # Get the current time
            current_time = time.time() - start

            # If the current minute is different from the minute of the last call, reset the call counter
            if current_time > 60:
                start = time.time()
                calls_in_current_minute = 0

            # If the call limit has been reached, return early
            if calls_in_current_minute >= calls_per_minute:
                print(f'call limit reach -- waiting for {(60 - current_time)}')
                time.sleep((60 - current_time))
                calls_in_current_minute = 0
            else:
                # Update the call counter and the last call time
                calls_in_current_minute += 1

            last_call_time = current_time

            # Call the original function
            return func(*args, **kwargs)

        return wrapper

    return decorator
