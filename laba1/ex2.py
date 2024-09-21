import string

vowel_str = 'ёуеоаыяию'
consonant_str = 'йцкнгшщзхъфвпрлджчсмтьб'

vowel_list = []
consonant_list = []


vowel_count = 0
consonant_count = 0

text = input("Введите текст")
print(text)

for el in text:
    if el in vowel_str:
        vowel_count += 1
        vowel_list.append(el)
    elif el in consonant_str:
        consonant_count += 1
print("Гласных: ", vowel_count, "Согласных: ", consonant_count)
if vowel_count == consonant_count:
    for el in vowel_list:
        print(el, end=' ')

wordCount = len(text.split())
print("В тексте", wordCount, "слов")




