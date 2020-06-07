import string

positif_words = open("positif_words.txt", encoding='utf-8').read().lower() \
.translate(str.maketrans('', '', string.punctuation + '…' + '\t')) \
.split()

negatif_words = open("negatif_words.txt", encoding='utf-8').read().lower() \
.translate(str.maketrans('', '', string.punctuation + '…' + '\t')) \
.split()

def weight_func(nameFile):
    weight = 0
    words_list = open(nameFile, encoding='utf-8').read().lower() \
    .translate(str.maketrans('', '', string.punctuation + '…' + '\n' \
    + '\t' + '0123456789')) \
    .split()

    for word in words_list:
        if word in positif_words:
            weight += 1
        elif word in negatif_words:
            weight -= 1
    return weight

weight = weight_func(input("Please enter the name of the file : "))
if weight > 0:
    print("The text is positif !")
else:
    print("The text is negatif !")
