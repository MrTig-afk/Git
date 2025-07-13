# Star pattern for the app.py file
def print_star_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
# Example usage
if __name__ == "__main__":
    n = 5  # You can change this value to print a larger or smaller star pattern
    print_star_pattern(n)   
    print("Star pattern printed successfully.")