"""
In this kata you will create a function that takes
a list of non-negative integers and strings and
returns a new list with the strings filtered out.

"""

def filter_list(l: list) -> list[int]:

    result = []

    for i in l:
        if type(i) != str:
            result.append(i)

    return result

if __name__ == "__main__":
    print(filter_list([1,'a','b',0,15]))
