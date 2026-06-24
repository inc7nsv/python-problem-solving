"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

"""

def get_friend(name: list[str]) -> list[str]:

    resul = []

    for i in name:
        if len(i) == 4:
            resul.append(i)

    return resul

if __name__ == "__main__":
    print(get_friend(["Peter", "Stephen", "Joe"]))