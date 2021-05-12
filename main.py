print("Welcome to Zayaan's Game!")
age = 13
low_age = age < 13
normal_age = age >= 13
if low_age == True:
  print("Sorry you are not old enough to play this game!")
else:
  print("Welcome to game! You are old enough to play this game!")
  print("Here are some questions! answer them to continue")
  print("Q.1. Where was the 2014 Soccer World Cup held at?")
  print("A) Africa")
  print("B) Italy")
  print("C) Brazil")
  print("D) Germany")
  answer = "Brazil"
  correct_answer = answer == "Brazil"

  print("Your answer: " + answer)
  if correct_answer == True:
   print("Congratualtions! You put in the correct answer! ")
  else:
    print("Sorry you put in the wrong answer! Try again")