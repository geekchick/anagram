
def checkAnagram(word1, word2):
    word2List = list(word2) # ['t', 'o', 'n', 'y', 'a']
    position = 0 #
    check1 = True
    while position < len(word1): # Keeps track of each letter in word1 to compare to letter in word2
        position2 = 0 # Reset position2 to start the while loop
        found = False
        while position2 < len(word2List) and not found: # Keeps track of each position in word2
            if word1[position] == word2List[position2]:
                found = True
            else:
                position2 = position2 + 1 # Go to the next letter in word2list
        if found:
            word2List[position2] = None # We have to reset the list
        else:
            check1 = False
        position = position + 1

    return check1

print(checkAnagram("heart", "earth"))