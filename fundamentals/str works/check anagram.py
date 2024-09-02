source_word="listen"
target_word="silent"

def anagram(word1,word2):
    return sorted(word1)==sorted(word2)

print(anagram(source_word,target_word))