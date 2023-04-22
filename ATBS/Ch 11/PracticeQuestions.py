# Write your code here :-)
import traceback, os, logging

from pathlib import Path

# 1
spam = 12
assert spam > 10, "Spam is less than 10"

# 2
eggs = "hello"
bacon = "HellO"

assert eggs.lower() == bacon.lower(), "Not the same"

# 3
# assert 0 == 1, 'Auto assertion error'


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string")
    if width < 2:
        raise Exception("Width must be greater than 2")
    if height <= 2:
        raise Exception("Height must be greater than 2")

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (("*", 4, 4), ("0", 20, 5)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print("An exception happened: " + str(err))


"""def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()"""

"""try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()"""

ages = [26, 17, 13]
ages.sort()
assert ages[0] < ages[-1], "First age is not less than last age"

logging.basicConfig(
    filename="myProgramLog.txt",
    level=logging.DEBUG,
    format=" $(asctime)s - %(levelname)s - %(message)s",
)
logging.debug("Start of program")


def factorial(n):
    logging.debug("Start of factorial(%s%%)" % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug("i is " + str(i) + ", total is " + str(total))
    logging.debug("End of factorial(%s%%)" % (n))
    return total


print(factorial(5))
logging.debug("End of program")
