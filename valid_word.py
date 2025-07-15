def valid_word(word):
    word = word.lower()
    vowels=set('aeiou')
    if word.isalnum() and len(word)>=3:
        for i in word:
            if i.isalpha() and  i in vowels:
                vowel = True
            elif i.isalpha() and i not in vowels:
                consonant = True
        if vowel and consonant:
            return True
    return False

word = input()
print(valid_word(word))
