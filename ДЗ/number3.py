from re import*

text = input("Введите текст: ")

words = findall(r'\w+',text)
words_usage_rate = {}

for word in words:
    if word not in words_usage_rate:
        words_usage_rate[word] = 1
    else:
        words_usage_rate[word]+=1

top_of_words = []

for word in words_usage_rate:
    top_of_words.append([words_usage_rate[word],word])

top_of_words.sort(reverse=True)

n = 0

for word in top_of_words:
    if n<5:
        print(word[1])
    n+=1