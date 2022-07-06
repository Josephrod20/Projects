#  Joseph Rodriguez
#  1904810
#  CSE 20 Fall 2021
#  pa3
#
#  Random
#  My program will generate a random integer from 1-n, where n isobtained by user
#  input.It then ask you to guess the number n amount of times.After each guess my
#  will tell you if the guess was correct,too high, or too low.
#-----------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements

from random import randint

#------------------------------------------------------------------------------
def main():
   print(" ")
   
   num=int(input("Enter a positive integer: "))
   answer=randint(1,num)
   
   print(" ")
   
   print("Try to guess my random integer in the range 1 to",num)
   print(" ")
   attempts=0
   EndGame = False
  
   while EndGame==False:
      attempts+=1
      print("Guess",attempts,end="")
      guess=int(input(": "))
            
      if guess==answer and attempts>1:
         print("  ",guess,"is correct, you found my number in",attempts,"guesses :)")
         EndGame==True
         break
      elif guess==answer and attempts==1 :
         print("  ",guess,"is correct, you found my number in",attempts,"guess :)")
         EndGame==True
         break
      if guess>answer :
         print("  ",guess,"is too high")
      elif guess<answer :
         print("  ",guess,"is too low")


   print(" ")
            
                  
   



# end

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end

   
