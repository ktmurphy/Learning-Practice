# Write your code here :-)
import random, logging, time

# logging.disable(logging.CRITICAL)

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("Start of program")
guess = ""

while guess not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
    logging.debug("Guess is: (%s%%)" % (guess))
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if guess == "heads":
    guess = 1
elif guess == "tails":
    guess = 0
logging.debug("Toss is: (%s%%)" % (toss))
if toss == guess:
    print("You got it")
    logging.debug("First If Statement: Toss and guess are: Toss - (%s%%)" % (toss))
    logging.debug("First If Statement Guess: (%s%%)" % (guess))
else:
    print("Nope! Guess again!")
    guess = input()
    if guess == "heads":
        guess = 1
    elif guess == "tails":
        guess = 0
    logging.debug("Second Guess: (%s%%)" % (guess))
    logging.debug("Second Toss - (%s%%)" % (toss))
    if toss == guess:
        print("You got it!")
        logging.debug("Second Statement Guess: (%s%%)" % (guess))
        logging.debug("Second statement Toss - (%s%%)" % (toss))
    else:
        print("Nope. You are really bad at this game.")
