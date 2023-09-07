#Dictionary Implementation

file_name = input("input filename: ")
file_handle = open(file_name)

#find all the words and record their occurence
counts = dict()
for line in file_handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#find the word with the most occurence
largest_word = None
largest_count = None
for (word, count) in counts.items():
    if largest_count is None or count > largest_count:
        largest_word = word
        largest_count = count

print(largest_word, largest_count)