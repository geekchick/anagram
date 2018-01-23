# Sort each word alphabetically and check if they're equal
# Algorithm
# 1. while the position of the word is less than the length of the word
# 2. Take the first letter in word and compare it to the second word
# 3  if the



def check_anagram(word1, word2):
    word1_check = sort_word(word1)
    word2_check = sort_word(word2)

    if word1_check == word2_check:
        return True
    else:
        return False




def sort_word(word):
    new_word = list(word)
    for i in range(1, len(new_word)):
        key = new_word[i]

        j = i - 1
        while j >= 0 and key < new_word[j]:
            new_word[j + 1] = new_word[j]
            j = j - 1
            new_word[j + 1] = key

    return new_word



print(check_anagram("heart", "earth"))