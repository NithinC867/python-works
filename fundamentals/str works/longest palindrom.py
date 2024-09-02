word="RACECAR"

for i in range(0,len(word)):
    left=i
    right=i
    while(word[left]==word[right] and left>=0 and right<len(word)):
        current_palindrome=word[left:right+1]
        print(current_palindrome)
        left=left-1
        right=right+1