import string
import sqlite3


def rot13(message):
    letters = string.ascii_lowercase * 2
    letters1 = string.ascii_uppercase * 2
    answer = []
    for let in message:
        if let.islower():
            answer.append(letters[letters.index(let) + 13])
        elif let.isupper():
            answer.append(letters1[letters1.index(let) + 13])
        else:
            answer.append(let)
    return ''.join(answer)

