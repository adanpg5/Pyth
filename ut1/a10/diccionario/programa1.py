import sys

sentence = sys.argv[1]


def count_words(sentence):
    palabras = sentence.split()
    summary = {}
    for palabra in palabras:
        if palabra in summary:
            summary[palabra] += 1
        else:
            summary[palabra] = 1
    return summary
for name, count in (count_words(sentence)).items():
    print(name + ":" + str(count))
