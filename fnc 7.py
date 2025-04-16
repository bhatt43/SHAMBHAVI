def ispalindrome(s):
  
    cleaned = ''.join(s.lower().split())
    
    return cleaned == cleaned[::-1]

text = input("Enter a word or phrase: ")

if ispalindrome(text):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
