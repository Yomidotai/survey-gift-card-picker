import random
lines = open('emails.csv').read().splitlines() # yes, this reads the whole file into memory... it's okay... we got enough
winner = random.choice(lines)
print(winner)
