# Prabdil Sandhu and Drew Soderquist
# CSC 321-05
# Assignment 4
# Task 2 with workfactor 10

from bcrypt import *
from nltk.corpus import words
import time

def main():
   start = time.time()
   pwList = words.words()
   pwList = [pw for pw in pwList if len(pw) in range(6, 11)]
   users = {
      b"$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom" : "Balin",
      b"$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be" : "Dwalin",
      b"$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK" : "Oin"
   }
   numInputs = 0
   found = 0
   while True:
      hash = hashpw(pwList[numInputs].encode(), b"$2b$10$xGKjb94iwmlth954hEaw3O")
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