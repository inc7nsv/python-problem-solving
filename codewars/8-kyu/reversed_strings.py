"""
Complete the solution so that it reverses
the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""

def solution(word: str) -> str:
    return word[::-1]

if __name__ == "__main__":
    print(solution("word"))