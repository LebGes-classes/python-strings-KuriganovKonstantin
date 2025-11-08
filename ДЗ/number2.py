from re import*
from string import*


text = ''
real_text = ''

while '.' not in text:
    additional_text = input('Введите текст: ' )
    text += additional_text

for letter in text:
    if '.' not in real_text:
        real_text += letter

words = findall(r'[a-zA-z]+',real_text)
real_words = []

for word in words:
    if len(word) <= 20:
        real_words.append(word)

K = 0

for word in real_words:
    K = max(K,len(word))

replaced_words = []
alphabet_uppercase = {}
alphabet_lowercase = {}
number = 0

for letter in ascii_uppercase:
    number+=1
    alphabet_uppercase[letter] = number

number = 0

for letter in ascii_lowercase:
    number+=1
    alphabet_lowercase[letter] = number

for word in words:
    replaced_word = ''

    for letter in word:
        if letter in ascii_uppercase:
            replaced_word+=ascii_uppercase[(alphabet_uppercase[letter]+K-1)%26]
        else:
            replaced_word += ascii_lowercase[(alphabet_lowercase[letter] + K-1)%26]

    replaced_words.append(replaced_word)

print(' '.join(replaced_words))
print(K)