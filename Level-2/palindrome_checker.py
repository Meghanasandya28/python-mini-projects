text = input("Enter string: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")