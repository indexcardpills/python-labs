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

short_words=len(min(words, key=len))
for s in words:
    if len(s)==short_words:
        print(s)
long_words=(len(max(words, key=len)))
for l in words:
    if len(l)==long_words:
        print(l)
print(len(words))

