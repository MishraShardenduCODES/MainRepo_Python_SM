def cd_lang_creator(a):
    word_length = len(a)
    salt = 'pbk' 
    if word_length >= 3:
        first_letter = a[0]
        a.pop(0)
        a.append(first_letter)
        a.insert(0, salt)
        a.append(salt) 
    else:
        a.reverse()
    secret_str = ''.join(a)
    return secret_str

def cd_lang_translator(b):
    word_length = len(b)
    if word_length < 3:
        b.reverse()
    else:
        b = b[3:-3]
        b.insert(0, b.pop())
    translated_str = ''.join(b) 
    return translated_str

sentence = str(input("Speak a sentence : "))
print('\n\n')

words = sentence.split()
secret_words = []
print("The secret code is : ", end='\n')
for word in words:
    word_list = list(word)
    secret_word = cd_lang_creator(word_list)
    secret_words.append(secret_word)
print(' '.join(secret_words), end='\n\n')

translated_words = []
print("This is translated as : ", end='\n')
for secret_word in secret_words:
    translated_word = list(secret_word)
    translated = cd_lang_translator(translated_word)
    translated_words.append(translated)
print(' '.join(translated_words))
