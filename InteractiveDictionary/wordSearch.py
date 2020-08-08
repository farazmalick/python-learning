import json
from difflib import get_close_matches

data = json.load(open("files/data.json"))


def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("Did you mean %s? enter y for yes n for no: " %
                       get_close_matches(word, data.keys())[0])
        if choice == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == "n":
            return "double check your word!"
        else:
            return "invalid choice"

    else:
        return "double check your word!"


word = input("enter word: ")

result = search(word)
i = 1
if isinstance(result, list):
    for r in result:
        print("%s-%s" % (i, r))
        i = i+1
else:
    print(result)
