import sys
if len(sys.argv) == 3:
    balance = float(sys.argv[1])
    deposit = float(sys.argv[2])
    print("User provided values:")
else:
    balance = 1000
    deposit = 500
    print("No input given - using default values:")

updated_balance = balance + deposit

print("Updated Balance:", updated_balance)
