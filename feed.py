import time

print("This is the feed back page")
rate = int(input("Rate the game out of 10: "))
if (rate >= 5):
  print("Thank you so much")
  wrong = "0"
else:
  wrong = input("What went wrong: ")
fb = input("Please write overall feedback: ")
print("Thank you for your feed back! We'll take it and improve our game. Have a nice day")

if (rate >= 5):
  time.sleep(7)
  print(" ")
  print(fb)
else: 
  time.sleep(7)
  print(" ")
  print(wrong)
  print(" ")
  print(fb)
