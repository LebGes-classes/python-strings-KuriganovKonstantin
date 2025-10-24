from re import*

text = input('Введите текст: ')

words = findall(r"\b\w+\b", text)
words_in_reverse_order = ''
text_in_reverse = ''
number = -1

for i in range(len(words)):
    words_in_reverse_order+= ( words[number] + ' ' )
    number -=1

number = -1

for i in range(len(text)):
    text_in_reverse += text[number]
    number -=1

print(words_in_reverse_order)
print(text_in_reverse)
