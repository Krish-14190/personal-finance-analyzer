def log_analysis(func):

    def wrapper(*args, **kwargs):
        print(f"[INFO] {func.__name__} started")

        result = func(*args, **kwargs)

        print(f"[INFO] {func.__name__} completed")

        return result

    return wrapper