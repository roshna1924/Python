# Write a python program to find the wordcount in a file for each line and then print the output.
# Finally store the output back to the file.

file = open("words.txt", 'r')
data = file.read()
words = data.split()

wordcount = [words.count(w) for w in words]     # Count the number of word frequency

for x in (zip(words, wordcount)):   # Zip used to combine two list
    print(x, file=open("output_wordcount.txt", "a"))

