import json


def function(fun):
    if fun == 1:
        reftype = input("type> ")
        lang = input("lang> ")
        author = input("type> ")
        title = input("type> ")

        with open("ref.json", "r") as fin:
            data = json.load(fin)

        new_ref = {"type": reftype, "lang": lang, "author": author, "title": title}
        data["references"].append(new_ref)

#        del data["references"][0]

        with open("ref.json", "w") as fout:
            fout.write(json.JSONEncoder().encode(data))

    elif fun == 2:
        print("123")

function(1)
