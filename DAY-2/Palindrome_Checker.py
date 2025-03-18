def is_palindrome(s):
    return s==s[::-1]

word = input("Enter a word: ").lower()
if is_palindrome(word):
    print(f"{word} is a Palindrome.")
else:
    print(f"{word} is not a Palindrome.")