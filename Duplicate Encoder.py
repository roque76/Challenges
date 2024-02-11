def duplicate_encode(word):
    wordList = list(word)
    out = []
    for char in wordList:
        print(char)
        for letter in wordList:
            if letter==char:
                print(f"match {letter}, {char}")


test1 = "Success"
test2 = "Theme"
test3 = "desync"

duplicate_encode(test1)
duplicate_encode(test2)
duplicate_encode(test3)
