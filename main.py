import random
lines = []
with open('emails.csv') as emails:
  lines = emails.readlines() # yes, this reads the whole file into memory... it's okay... we got enough

winner = random.choice(lines)
print(winner)
