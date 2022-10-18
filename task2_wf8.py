# Prabdil Sandhu and Drew Soderquist
# CSC 321-05
# Assignment 4
# Task 2 with workfactor 8

from bcrypt import *
from nltk.corpus import words
import time

def main():
   start = time.time()
   pwList = words.words()
   pwList = [pw for pw in pwList if len(pw) in range(6, 11)]
   users = {
      b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC" : "Gandalf",
      b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q" : "Thorin"
   }
   numInputs = 0
   found = 0
   while True:
      hash = hashpw(pwList[numInputs].encode(), b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.")
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