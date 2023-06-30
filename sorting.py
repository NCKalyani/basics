def sorting_string(sentence):
    words = sentence.split()
    return ''.join(sort(words, key=str.casefold))


if __name__ == '__main__':
    print(sorting_string("FISH banana Apple ORANGE")
     
