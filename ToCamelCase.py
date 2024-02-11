def stringChanger(text):
    if not "-" and "_" not in text:
        return text
    else:
        textList = list(text)
        for charIndex in range(len(text)):
            if textList[charIndex] == "_" or textList[charIndex] == "-":
                textList[charIndex+1] = textList[charIndex+1].upper()
                print(textList)

        textList = [char for char in textList if char not in ['-','_']]

        return ''.join(textList)


test = "the-Stealth_warrior"
test2 = "A-B-C"
test3 = "the-cute-CAt"

out1 = stringChanger(test)
out2 = stringChanger(test2)
out3 = stringChanger(test3)

