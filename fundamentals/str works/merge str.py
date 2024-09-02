# word1="pqr"
# word2="abc"

# merged_str=""

# for i in range(0,len(word1)):

#     merged_str=merged_str+word1[i]+word2[i]

# print(merged_str)


word1="PQRS"
word2="ABCDEFG"

smallest_word=word1 if len(word1)<len(word2) else word2

merge_str=""

for i in range(0,len(smallest_word)):
    