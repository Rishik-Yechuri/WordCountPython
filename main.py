from collections import Counter

# opens the file called Quickstart.dat
file = open('Quickstart.dat')
# Creates a list of words that need to be removed
wordsToRemove = ["for", "and", "nor", "but", "or", "yet", "so"]
# Creates an array that stores all the words from the file
words = file.read().split()
# stores the original size of the array(isn't used,since program wasn't done 100% properly)
size = len(words)


# function to completely remove a value from an array
# Returns an array,and the parameters are:(ArrayToRemoveFrom,WordToRemove)
def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


# Loops through the words to remove array
for x in wordsToRemove:
    # removes the words from the array
    words = remove_values_from_list(words, x)
# creates a counter,which is used to easily display info
words_to_count = (word for word in words)
c = Counter(words_to_count)
# gets the 20 most common words
mostCommon = c.most_common(20)
# prints out mostCommon,prints [WORD] + [COUNT]
# Doesn't display percentages,since I couldn't figure that out
print(mostCommon)
