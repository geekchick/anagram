# Count letters in each word and compare to letters in second word

# Algorithm
# 1. Take first letter in word 1 list
# 2. Check to see if it's equal to all the letters in the word
# 3. If it's equal then add 1 count
# 4. If it's not equal then go to the next letter

def checkAnagram(word):
    wordList = list(word)
    position = 0
    nextPosition = 0
    count = 0
    wordDict = {}

    for letter in wordList:
        if letter not in wordDict:
            while nextPosition < len(word): # Checks if the legnth of word1 is less than the position
                #print("nextPosition {} and length of word1 {}".format(nextPosition, len(word1)))
                if letter == wordList[nextPosition]: # Compares letter in word1 to next letter in word1
                    count = count + 1 # If the letter is the same then add 1 to count
                    nextPosition = nextPosition + 1 # Go to next letter in word1
                else:
                    nextPosition = nextPosition + 1 # if the letter is not the same then go to next letter in word1
            wordDict[letter] = count
            #print("This is my dict {}".format(wordDict))
        #print("{} has {} letters".format(letter, count))
        nextPosition = 0
        count = 0

    return wordDict

def checkWord(word1, word2):
    checkWord1 = checkAnagram(word1)
    checkWord2 = checkAnagram(word2)

    if checkWord1 == checkWord2:
        return True
    else:
        return False


#print(checkAnagram('hhrart'))
print(checkWord('hraet','hearto'))

#heart | earth
