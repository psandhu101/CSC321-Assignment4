# Prabdil Sandhu and Drew Soderquist
# CSC 321-05
# Assignment 4
# Task 1

from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import time

def arbitraryHashPrint(userInput):
   a = SHA256.new() 
   a.update(userInput)
   aSHA = a.hexdigest()

   print("SHA256 Hash: ", aSHA)

def arbitraryHashReturn(userInput):
   a = SHA256.new() 
   a.update(userInput)
   aSHA = a.hexdigest()[:7] # truncate

   return aSHA

def main():
   # ham1 = b'0000'
   # ham2 = b'0001'
   # arbitraryHashPrint(ham1)
   # arbitraryHashPrint(ham2)
   m0 = get_random_bytes(16)
   m0Hash = arbitraryHashReturn(m0)
   start = time.time()
   numInputs = 0
   while True:
      numInputs += 1
      m1 = get_random_bytes(16)
      if (m0 != m1):
         m1Hash = arbitraryHashReturn(m1)
         if (m1Hash == m0Hash):
            end = time.time()
            print("Collision: " + m1Hash + " (" + str(len(m1Hash) * 4) + " bits)")
            print("numInputs: " + str(numInputs))
            print("Time Passed: " + str(end - start) + " seconds")
            return

if __name__ == "__main__":
   main()