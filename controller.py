import pydirectinput
import time


def type_this(word: str) :
    time.sleep(3)
    pydirectinput.keyDown('enter')
    pydirectinput.keyUp('enter')
    for letter in word :
        pydirectinput.keyDown(letter)
        pydirectinput.keyUp(letter)


if __name__ == '__main__' :
    type_this("Testing.....123")