# function replaces vowels with the letter "g"

def translate(phrase):
    new_word = ""
    for i in phrase:
        if i in "AEIOUaeiou":
            new_word += "g"
        else:
            new_word += i
    return new_word

print(translate(input("enter a word: ")))
