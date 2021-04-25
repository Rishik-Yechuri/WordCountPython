from collections import Counter

file = open('Quickstart.dat')
wordsToRemove = ["for", "and", "nor", "but", "or", "yet", "so"]
words = file.read().split()
size = len(words)


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


for x in wordsToRemove:
    words = remove_values_from_list(words, x)
words_to_count = (word for word in words)
c = Counter(words_to_count)
mostCommon = c.most_common(20)
print(mostCommon)