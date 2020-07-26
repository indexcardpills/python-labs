'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
words=[]
with open('words.txt', 'r') as fin:
    for word in fin.readlines():
        word=word.rstrip()
        words.append(word)

length_of_shortest_words=len(min(words, key=len))
length_of_longest_words=(len(max(words, key=len)))
short=[]
long=[]
for word in words:
    if len(word)==length_of_shortest_words:
        short.append(word)
    if len(word)==length_of_longest_words:
        long.append(word)
print(short)
print(long)


print(len(words))

