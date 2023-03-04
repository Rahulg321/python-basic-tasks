
def replace_word():
    str = 'Hello I am in Love and again and again'
    
    word_to_replace = input('Enter the word to replace ')
    word = input('Enter the new word to be put in the place ')
    
    print(str.replace(word_to_replace,word))



def main():
    replace_word()


main()