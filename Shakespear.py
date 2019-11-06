import csv
opened_file = open('Documents/shakespeare.txt')
text_data = list(opened_file)

# not sure if these should be removed from words -- punctuation=['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
punctuation=['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", "-", "[", "]", "*", "&", "<", ">", "_", "#", "{", \
             "~", "}"]
new_text_data = []
# This for loop removes items in the punctuation list and creates a new_text_data
for i in range(len(text_data)):
    result = ""
    for character in text_data[i]:
        if(character not in punctuation):
            result += character
    new_text_data.append(result)

# The following creates a dictionary of words and frequencies from the shakespeare text file
word_counting = {}

for line in new_text_data:
    words = line.split()
    for word in words:
        if word.lower() in word_counting:
            word_counting[word.lower()] += 1
        else:
            word_counting[word.lower()] = 1

print(word_counting)

sorted_word_counting = dict(sorted(word_counting.items()))
sorted_word_counting = dict(sorted(word_counting.items()))
print(sorted_word_counting)

with open('shakes_word_count.csv', 'w') as csv_file:
    [csv_file.write('{0},{1}\n'.format(key, value)) for key, value in sorted_word_counting.items()]


opened_file.close()
csv_file.close()
