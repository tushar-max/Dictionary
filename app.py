import json
from difflib import get_close_matches


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes, or N for no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist please recheck it"
        else:
            return "Error"
    else:
        return "Word doesn't exists."


def translate_app(w):
    data = json.load(open("data.json"))
    w = w.lower()
    if w in data:
        return data[w][0]
    elif w.capitalize() in data:
        return data[w.capitalize()][0]
    elif w.upper() in data:
        return data[w.upper()][0]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:
        return "Word doesn't exists."


if __name__ == '__main__':
    data = json.load(open("data.json"))
    word = input("Input word")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
