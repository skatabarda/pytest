first_word = "eadwewt"
second_word = "tea"

# Найти сколько одинаковых символов есть в словах

char_count = 0

for char in first_word:
    if char in second_word:
        char_count += 1
print("Same chars:", char_count)


