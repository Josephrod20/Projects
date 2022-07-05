
#------------------------------------------------------------------------------
#  ScrabbleTemplate.py
#------------------------------------------------------------------------------

def norm(s):
   """
   Returns the norm of a string obtained by alphabetizing its characters.
   """
   l = list(s)
   l.sort()
   b = "".join(l)
   return b


# end norm()

def AnagramDictionary(f, d):
   """
   Returns a dictionary whose keys are the norms of the words in file f, and 
   whose values are lists of words with a given norm. Thus each list contains
   a group of words in f that are anagrams of each other.
   """
   
   y = []
   count = 0
   for line in f:
      l = sorted(str(line.strip(string.whitespace)))
      b = "".join(l)
      count += 1
      if b not in d:
         y=[]
         d[b] = y
         y.append(str(line.strip(string.whitespace)))
      else:
         y = []
         y.append(str(line.strip(string.whitespace)))
         d[b] += y
         
         
   return d         

  


# end AnagramDictionary()

def printWordList(L):
   """Prints the words in L on a single line, separated by commas."""
   
   print(", ".join(L)) 


# end printWordList()
import sys
import string
# main() ----------------------------------------------------------------------
def main():
   # open a word file, assemble the dictionary using words, close file
   f = open(scrabble.txt)
   d = dict()
   AnagramDictionary(f, d)
   # get input from user, and query the dictionary
   print()
   s = str(input("Enter a string (or nothing to quit): "))
   if s == " ":
      s = str(input("Enter a string (or nothing to quit): "))  
   while s != "":
      # get a string from the user
      print()
      norm(s)
      # look up string in the dictionary, print its anagrams if they exist
      if norm(s) not in d:
         print("The letters in '"+(s)+"' do not form a word in the dictionary")
         print()
         s = str(input("Enter a string (or nothing to quit): "))
         continue
      for i in d:
         if i == norm(s):
            L = d[i]
               
      print("The anagrams of "+str(s),"are:")   
      printWordList(L)
      print()
      s = str(input("Enter a string (or nothing to quit): "))
      
      
   print()   
   print("Bye!")
   print()
         
         

# end main() ------------------------------------------------------------------


# -----------------------------------------------------------------------------
if(__name__=='__main__'):

   main()

# end if --------------------------------------------------------------------
