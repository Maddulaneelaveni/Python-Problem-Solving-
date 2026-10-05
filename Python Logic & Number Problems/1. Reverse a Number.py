# 1 — Reverse a Number
# Definition
# Reversing a number means arranging its digits in the opposite order.
# Example: 12345 → 54321

# Input from user
num=int(input("Enter a number : "))
# Store the reversed number
reverse = 0
# Continue until all digits are processed
while num>0:
    # Get the last digit of a number
    digit=num%10
    # Add the last digiy to the reversed number
    reverse=reverse*10+digit
    # Remove the last digit from the original number
    num =  num//10
# Display the reversed number
print("Reversed Number:",reverse)
