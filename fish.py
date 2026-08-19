import time
import random

numFish = 0 #trh ammount of fish you caght
money = 0
moneyMade = 0

luck = 0 #wether u get a fish or not
min = 1 #min $money
max = 10 #max $money

minCost = 10
maxCost = 10

quitGame = 0


print("hello! this is a small terminal game about fishing.\n")

def start():
  print("what would you like to do?")
  print(" open shop (s)\n show stats (m)\n go fishing (f)\n quit game (q)")

  option = input("-- ")

  if(option == "s"):
    print("\nyou selected shop\n")
    shop()

  elif(option == "m"):
    print("\nyou selected stats")
    print("money = ", money)
    print("min = ", min)
    print("max = ", max)
    print("fish caught = ", numFish, "\n")

  elif(option == "f"):
    print("\nyou selected fishing")
    fish()

  elif(option == "q"):
    print("\n\ngoodbye. have a great day.\n")
    global quitGame
    quitGame = 1

  else:
    print("\ninvalid option")
    print("try again\n")

def fish():
  print("you cast your line...")
  time.sleep(1)
  print("you wait")
  time.sleep(2)
  luck = random.randint(1, 4)

  if(luck >= 1):
    print("you caught the fish")
    moneyMade = random.randint(min, max)
    print("you made", moneyMade, "money\n\n")
    global money
    global numFish
    money += moneyMade
    moneyMade = 0
    numFish += 1

  else:
    print("you lost the fish\n")

def shop():
  print("you selected the shop")
  global money
  global maxCost
  global minCost
  global min
  global max
  print("you can uprade your...")
  print("min for", minCost, "money  (i)")
  print("max for", maxCost, "money (a)")

  selec = input("-- ")

  if(selec == "i"):
    if(money >= minCost):
      if(max > min):
        money -= minCost
        minCost *= 2
        #minCost += 0
        min += 1
        print("\nyou increase your min to", min)
        print("min now cost", minCost)
        print("you have", money, "money left\n")

      else:
        print("\nyour min is to high, try upgrading your max first\n")
    else:
      print("\nyou dont have enough money\n")


  elif(selec == "a"):
    if(money >= maxCost):
      money -= maxCost
      maxCost *= 2
      max += 1
      print("\nyour max is now", max)
      print("max now cost", maxCost)
      print("you have", money, "money left\n")

  else:
    print("\ninvalid option")
    print("try again \n")

while(quitGame == 0):
  start()

