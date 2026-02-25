
def VowelOrConsonent(letter):
    res = letter.lower()

    if len(res) != 1 or not res.isalpha():
        return "Invalid Input"
    elif res in 'aeiou':
        return "Vowel"
    else: return "Consonent"

print(VowelOrConsonent(input('Enter the letter: ')))