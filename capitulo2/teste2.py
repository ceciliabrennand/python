import random

input('Ask the Magic 8 Ball a question: ')

resp = random.randint(1, 9)

if resp == 1:
    print('Magic 8 Ball: Yes - definitely.')
elif resp == 2:
  print('Magic 8 Ball: It is decidedly so.')
elif resp == 3:
  print('Magic 8 Ball: Without a doubt.')
elif resp == 4:
  print('Magic 8 Ball: Reply hazy, try again.')
elif resp == 5:
  print('Magic 8 Ball: Ask again later.')
elif resp == 6:
  print('Magic 8 Ball: Better not tell you now.')
elif resp == 7:
  print('Magic 8 Ball: My sources say no.')
elif resp == 8:
  print('Magic 8 Ball: Outlook not so good.')
else:
  print('Magic 8 Ball: Very doubtful.')
  