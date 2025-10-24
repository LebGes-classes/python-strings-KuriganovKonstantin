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

for i in range(len(top_of_words)):
    for j in range(len(top_of_words)-1):
        cnt = top_of_words[j][0]
        cnt1 = top_of_words[j+1][0]

        if cnt < cnt1:
            better_word = top_of_words[j+1]
            top_of_words[j+1] = top_of_words[j]
            top_of_words[j] = better_word


n = 0

for word in top_of_words:
    if n<5:
        print(word[1])
    n+=1