#1-  Count Number of Lines in a File
#2- Search for a String in Text Files
#3- Find the most repeated word in a text file
#4- How to read specific lines from a File in Python?
#5- To count and display the total number of words in a text file.
#6- To count uppercase character in a text file

file = open("first.txt")
#lines = file.readlines()
#print(len(lines))
#content = file.read()
#words = content.split()
#print(len(words))
#p = file.readlines()
#print(p[2])

repeated_word = ""
repeat = 0
words = []

for line in file:
  line_word = line.lower().replace(',','').split()
  for w in line_word:
    words.append(w)

for i in range(0, len(words)):
  count = 1
  for j in range(i+1, len(words)):
    if words[i] == words[j]:
      count += 1
  print(count)
  if count > repeat:
    repeat = count
    repeated_word = words[i]

print("Most repeated word: " + repeated_word)
print("Frequency: " + str(repeat))
file.close();


