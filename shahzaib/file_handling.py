#File Handling

file = open("first.txt")

#1.Count Number of Lines in a File
lines = file.readlines()
print(len(lines))

#2.Search for a String in Text Files
content = file.read()
word = "Muhammad Shahzaib"
if word in content:
  print("String Found")
else:
  print("String Not Found")

#3.Find the most repeated word in a text file
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
  
  if count > repeat:
    repeat = count
    repeated_word = words[i]

print("Most repeated word: " + repeated_word)
print("Frequency: " + str(repeat))


#4.How to read specific lines from a File in Python?
p = file.readlines()
print(p[2:5])


#5.To count and display the total number of words in a text file.
content = file.read()
words = content.split()
print(len(words))

#6.To count uppercase character in a text file

cont = file.read()
for x in cont:
  upper_count = 0
  if x.isupper():
    upper_count += 1

print("Uppercase",count)