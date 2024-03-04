# palindrome number

n = int(input("enter a number: "))
copy = n
rev = 0

while n > 0:
    rev = rev*10 + n % 10
    n = n // 10

if rev == copy:
    print("number is palindrome")
else:
    print("number not palindrome ")
