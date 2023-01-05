#Поисковый алгоритм
def ss (number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found
numbers = range(0, 100)
s1 = ss(numbers, 202)
print(s1)
s2 = ss(numbers, 22)
print(s2)
#Палиндром
def palindrome(word):
    word = word.lower()
    return word[::-1] == word
print(palindrome("mama"))
print((palindrome("mam")))
#Анаграмма
def anagramm(w1,w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)
print(anagramm("тапок", "капот"))
print(anagramm("list", "derevo"))
#Анограмма
def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)
count_characters("Династия")

