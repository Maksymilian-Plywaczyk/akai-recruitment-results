# coding=utf-8
from collections import Counter
from operator import itemgetter

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]


def most_repeated_words(sentences: list, number_of_words: int) -> list[tuple]:
    list_with_seperated_word = []
    for x in sentences:
        word_list = x.split()
        list_with_seperated_word += word_list

    result = Counter(list_with_seperated_word).most_common(number_of_words)
    return result


def most_repeated_words_dict(sentences: list) -> list[tuple]:
    list_with_seperated_word = []
    words_dictionary = {}
    for x in sentences:
        word_list = x.split()
        list_with_seperated_word += word_list

    for word in list_with_seperated_word:
        if word in words_dictionary.keys():
            words_dictionary[word] += 1
        else:
            words_dictionary[word] = 1
    result = sorted(words_dictionary.items(), key=itemgetter(1), reverse=True)
    return result


def print_results(result: list[tuple]) -> None:
    print(f'1. "{result[0][0]}" - {result[0][1]}')
    print(f'2. "{result[1][0]}" - {result[1][1]}')
    print(f'3. "{result[2][0]}" - {result[2][1]}')


if __name__ == '__main__':
    while True:
        choose_number = input("Which implementation do you choose (1 or 2): ")
        if int(choose_number) == 1:
            result = most_repeated_words(sentences, 3)
            print_results(result)
            break
        elif int(choose_number) == 2:
            result = most_repeated_words_dict(sentences)
            print_results(result)
            break
        else:
            print('You can only pass 1 or 2')
            continue

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2
# 1. "nie" - 4
# 2. "jak" - 3
# 3. "Gdzie" - 3



# Good luck! You can write all the code in this file.
