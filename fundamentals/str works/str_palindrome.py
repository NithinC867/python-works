def palindrome(word):
    reverse=word[::-1]
    return word==reverse
print(palindrome("madam"))