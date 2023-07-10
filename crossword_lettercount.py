wordbank = "fsdlfkjsdvoisejrlsdkjfsldkfjsdlfkvnvinreuojsdfljgewknrweifdosfusodifjwerljewlkjdflkjdlfsjdofiefjwekvjnrvkjfoiejfslifjelfjndflnjk"
letter_array =[]
letter_array_totals = []
for letter in wordbank:
    if letter not in letter_array: 
      letter_array.append(letter)

for letter in sorted(letter_array):
  count = wordbank.count(letter)
  letter_array_totals.append("{letter} = {count}".format(letter=letter.upper(),count=count))

#for i in letter_array_totals:
#  print(i)

word_string = ""
for i in range(0,(len(letter_array_totals))):
   if letter_array_totals[i] != letter_array_totals[-1]:
        word_string += str(letter_array_totals[i]) + ", "
   else:
      word_string += str(letter_array_totals[i]) + "."

print(word_string)