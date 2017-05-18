try:
    words_filename = input()
    word_to_check = input()
    word_to_check_sorted = sorted(word_to_check)

    anagrams = []
    with open(words_filename, encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            if word != word_to_check and word_to_check_sorted == sorted(word):
                anagrams.append(word)

    if anagrams:
        anagrams.sort()
        for a in anagrams:
            print(a)
    else:
        print("NO ANAGRAMS")

except:
    print("INVALID INPUT")