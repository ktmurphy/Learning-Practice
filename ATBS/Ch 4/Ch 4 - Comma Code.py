#! python3
# turns list into a string with commas between list items
longList = ["ant", "dog", "tree"]
shortList = ["ant"]
noList = []


def stringMaker(lst):
    if len(lst) > 1:
        string = ""
        for item in lst:
            string = string + item + ", "
        return string
    elif len(lst) == 1:
        return lst[0]
    else:
        return " "


print(stringMaker(longList))
print(stringMaker(shortList))
print(stringMaker(noList))
