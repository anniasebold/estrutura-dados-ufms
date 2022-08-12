word = input()
word = word.lower()

a = 0
e = 0
i = 0
o = 0
u = 0

j = 0

while j < len(word):
  if (word[j] == 'a'):
    a += 1
  if (word[j] == 'e'):
    e += 1
  if (word[j] == 'i'):
    i += 1
  if (word[j] == 'o'):
    o += 1
  if (word[j] == 'u'):
    u += 1
  j = j + 1


print("a = " +  str(a))
print("e = " +  str(e))
print("i = " +  str(i))
print("o = " +  str(o))
print("u = " +  str(u))