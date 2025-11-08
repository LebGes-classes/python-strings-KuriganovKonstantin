from re import*


text = input('Введите текст: ')

words = findall(r"\b\w+\b", text)
words_in_reverse_order = ''
text_in_reverse = ''
n = len(words) - 1

for i in words:
    words_in_reverse_order+= ( words[n] + ' ' )
    n -=1

n = len(text) - 1

for i in text:
    text_in_reverse += text[n]
    n -=1

print(words_in_reverse_order)
print(text_in_reverse)
