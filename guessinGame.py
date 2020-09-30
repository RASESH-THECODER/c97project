import random 

def generateRandomNumber():
    randomNumber=random.randInt( 1 , 100 )
    return randomNumber

def askUserForNumber():
  userNumber = int(input( "Guess the numbers: "))
  return userNumber 
  def checkUserNumber(userNumber, randomNumber):
      if userNumber > randomNumber:
          return "Too High"
 elif userNumber < randomNumber:
     return "Too Low "
     else:
         return "Congratulations!"
 
 def main():
     randomNumber = generateRandomNumber()
     userNumber = askUserForNumber()
     message = checkUserNumber(userNumber, randomNumber)

     while message != "Congrulations":
         print( message )
         userNumber = askUserForNumber( "Try Again" )    