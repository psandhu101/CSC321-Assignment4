# Prabdil Sandhu and Drew Soderquist
# CSC 321-05
# Assignment 4
# Task 2 with workfactor 11

from bcrypt import *
from nltk.corpus import words
import time

def main():
   start = time.time()
   pwList = words.words()
   pwList = [pw for pw in pwList if len(pw) in range(6, 11)]
   users = {
      b"$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q" : "Gloin",
      b"$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq" : "Dori",
      b"$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12" : "Nori"
   }
   numInputs = 0
   found = 0
   while True:
      hash = hashpw(pwList[numInputs].encode(), b"$2b$11$/8UByex2ktrWATZOBLZ0Du")
      user = users.get(hash)
      if (user != None):
         end = time.time()
         print("User: " + user)
         print("Password: " + pwList[numInputs])
         print("Time Passed: " + str(end - start) + " seconds\n")
         found += 1
         if (found == len(users)):
            return
      numInputs += 1

if __name__ == "__main__":
   main()