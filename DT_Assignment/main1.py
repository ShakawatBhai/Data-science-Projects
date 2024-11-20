# Read input values
N = int(input())            # Number of elements
a = list(map(int, input().split()))  # List of integers

# Use a set to find unique integers
unique_integers = set(a)

# Output the number of unique integers
print(len(unique_integers))
