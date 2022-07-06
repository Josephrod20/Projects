#------------------------------------------------------------------------------
#  SieveTemplate.py
#------------------------------------------------------------------------------



def makeSieve(n):
   S=[True]*(n+1)
   
   S[0]=False
   S[1]=False

   
   for i in range(2,n+1):
      if S[i]:
         for x in range(i*i,n+1,i):
            S[x]=False
   return S
   

   
  


   
   
# end makeSieve()


def getIndices(L, x):
   indent=10
   primes=[]
   comp=[]
  
   if x==True:
      
      for i in range(len(L)):
         if(L[i]==True):
            primes.append(i)
      print("\nThere are",len(primes),"prime numbers in the range 1 to",(len(L)-1),end=":\n\n")
  
    
      for i in range(0,len(primes),indent):
         print(*primes[i:i+indent],"")

   if x==False:
      for i in range(len(L)):
         if (L[i]==False):
            comp.append(i)
      comp.remove(0)
      print("\nThere are",len(comp),"composite numbers in the range 1 to",(len(L)-1),end=":\n\n")
      
      for i in range(0,len(comp),indent):
         print(*comp[i:i+indent],"")
      print("")
# end getIndices()


# function main() -------------------------------------------------------------
def main():
   
   num=int(input("\nEnter a positive integer: "))

   while num<=0 :
      num=int(input("Please enter a positive integer: "))
   
   S=makeSieve(num)
   makeSieve(num)
   
   getIndices(S,True)
   # call makeSieve()
   getIndices(S,False)
   
   # call getIndices() to get a list of primes

   # call getIndices() to get a list of composites

   # print out the list of primes

   # print out the list of composites

# end main() ------------------------------------------------------------------

# closing conditional ---------------------------------------------------------
if __name__=='__main__':

   main()

# end if

