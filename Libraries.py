#import random
#from random import choice 
#coin=choice(["heads","tails"])

#print(coin)
#import random

#n=["jack","queen","king"]
#random.shuffle(n)

#for i in n:
#    print()

#n= random.randint(1,10)
#print(n)

import statistics

print(statistics.mean([100,90]))

import sys
if len(sys.argv)<2:
    sys.exit("too few argumenst")
elif len(sys.argv)>2:
    sys.exit("too many argumnets")
else:
    print("hello my name is", sys.argv[1])


import sys 
if len(sys.argv)<2:
    sys.exit("too few argumnets")
for arg in sys.argv[1:]:
    print("Hello my name is ",arg)