import random

name = "Paulo"
question = name + ", the question to win ten dollars is: "

if name == "":
  print(", The Question to Win ten dollars is:")
else:
  print(question)

if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
  



answer = ""

random_number = random.randint(1, 15)


if random_number == 1:
  answer = ("Yes - definitely.")
elif random_number == 2:
  answer = ("It is decidedly so.")
elif random_number == 3:
  answer = ("Without a doubt.")  
elif random_number == 4:
  answer = ("Reply hazy, try again")  
elif random_number == 5:
  answer = ("Ask again later.")  
elif random_number == 6:
  answer = ("Better not tell you now.")  
elif random_number == 7:
  answer = ("My sources say no.")  
elif random_number == 8:
  answer = ("Outlook not so good.")  
elif random_number == 9:
  answer = ("Very doubtful.")  
elif random_number == 10:
  answer = ("Why do you keep trying")
elif random_number == 11:
  answer = ("Why do you keep trying")  
elif random_number == 12:
  answer = ("Why do you keep trying")
elif random_number == 13:
  answer = ("Why do you keep trying")
elif random_number == 14:
  answer = ("Why do you keep trying")
elif random_number == 15:
  answer = ("Why do you keep trying")
else:
  answer ="Error"

print ("Magic 8-Ball´s answer: " + answer )