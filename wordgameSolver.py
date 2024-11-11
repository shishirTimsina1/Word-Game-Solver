import json

DICTIONARY_NAME = 'words_dictionary.json'
SCRABBLE_DICT = 'scrabbleDict.json'

# TODO: functionality will be press 1 for NYT spelling bee, 2 for word check for scrabble, 3 for word cookies etc
MAIN_MENU = (
'''======================================================================
\tEnter 1 for NYT Spelling Bee Solver
\tEnter 2 for Word check for Scrabble etc
\tEnter 3 for Word Cookies and similar games solver
======================================================================
Please type an option from the list above:
>>> ''')

BEE_MENU = (
'''======================================================================
\tEnter the string of letters, comma separated. ex (h,a,p,e,y,n,i)
======================================================================
Please type an option from the list above:
>>> ''')

def load_words(mode):
    if mode == 1:
        file = open(DICTIONARY_NAME)
        data = json.load(file)
        file.close()
        return data
    elif mode == 2:
        file = open(SCRABBLE_DICT)
        data = json.load(file)
        file.close()
        return data
    else:
        return

def pruneDictionary(letters, english_words, middleLetter):
    count = 0
    listWords = english_words.keys()
    listRemoveWords = []
    for word in listWords:
        if(len(word) < 4):
            listRemoveWords.append(word)
            count += 1
    for w2 in listRemoveWords:
        del english_words[w2]
    print('Removed {} words that were less than 4 letters'.format(count))

    listWords = english_words.keys()
    listRemoveWords = []
    for word in listWords:
        if all(c in letters for c in word):
            continue
        else:
            listRemoveWords.append(word)
    for w3 in listRemoveWords:
        del english_words[w3]

    listWords = english_words.keys()
    listRemoveWords = []
    for word in listWords:
        if middleLetter in word:
            continue
        else:
            listRemoveWords.append(word)
    for w3 in listRemoveWords:
        del english_words[w3]

def spellingBee():
    mode = 1
    english_words = load_words(mode)
    action = input(BEE_MENU)
    inputList = list(set(action.split(",")))
    middleLetter = input("What is the middle Letter?: ")
    pruneDictionary(inputList, english_words, middleLetter)
    print(english_words.keys())
    print(len(english_words))
    

def scrabbleCheck():
    mode = 2
    english_words = load_words(mode)
    action = input("Enter the Word you would like to search: ")
    if action.lower() in english_words:
        print("\n\t****************\n\t RESULT: \n\t Word Exists \n\t****************\n")
    else:
        print("\n\t****************\n\t RESULT: \n\t Word Does Not Exist \n\t****************\n")

def wordCookies():
    print("wordCookies Not implemented yet")

if __name__ == '__main__':
    while True:
        action = input(MAIN_MENU)
        if action == '1':
            spellingBee()
        elif action == '2':
            scrabbleCheck()
        elif action == '3':
            wordCookies()
        else:
            print('"{}" is not a valid action. Goodbye!'.format(action))
            break
