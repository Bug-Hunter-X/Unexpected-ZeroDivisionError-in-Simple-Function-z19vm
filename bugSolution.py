def function_with_uncommon_error(x):
    try:
        if x == 0:
            return float('inf')  # Handle division by zero gracefully
        else:
            return x + 5
    except Exception as e:
        print(f"An error occurred: {e}")
        return None # or some default value