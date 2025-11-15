import sys

def calculate_simple_interest(principal, rate, time):
    # Calculate Simple Interest
    si = (principal * rate * time) / 100

    print(f"Principal Amount : {principal}")
    print(f"Rate of Interest : {rate}")
    print(f"Time Period      : {time}")
    print(f"Simple Interest  : {si:.2f}")

# Check if user provided exactly 3 arguments
if len(sys.argv) != 4:
    print("Usage: python program.py <principal> <rate> <time>")
    sys.exit(1)

# Convert command-line arguments to float
principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

# Function Call
calculate_simple_interest(principal, rate, time)
