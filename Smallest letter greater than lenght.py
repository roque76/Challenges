
def nextGreatestLetter(letters, target):
    targ = ord(target.lower()) - ord('a') +1
    if targ == 26:
        return letters[0]
    output_number = 27
    for letter in letters:
        letter_number = ord(letter.lower()) - ord('a') + 1
        if letter_number>targ and letter_number<output_number:
            output_number = letter_number
        if output_number == 27:
            return letters[0]
    return chr(ord('a') + output_number-1)



