import time
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('=============')
print(' Sorting Hat')
print('=============')
print()

# Câu hỏi một #
print("Q1) Do you like Dawn or Duck?")
print('    1) Dawn')
print('    2) Dusk')
answer = int(input('Enter your answer (1-4): '))
if answer ==1:
  Gryffindor = Gryffindor +1
  Ravenclaw  = Ravenclaw +1
elif answer ==2:
  Hufflepuff = Hufflepuff +1
  Slytherin = Slytherin +1
else:
 print('Wrong input')
print()
# Câu hỏi hai #
print('Q2) When I’m dead, I want people to remember me as:')
print()
print('     1) The Good')
print('     2) The Great')
print('     3) The Wise')
print('     4) The Bold')
answer = int(input(" Enter the answer (1-4):"))
if answer ==1:
  Hufflepuff = Hufflepuff +2
elif answer ==2:
  Slytherin = Slytherin +2
elif answer ==3:
  Ravenclaw = Ravenclaw +2
elif answer ==4:
  Gryffindor = Gryffindor +2
else:
 print('Wrong input')
print()
print()
# câu hỏi 3 #
print('Q3) Which kind of instrument most pleases your ear?')
print()
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')
answer = int(input('Enter your answer (1-4):'))
if answer ==1:
  Slytherin = Slytherin +4
elif answer ==2:
   Hufflepuff = Hufflepuff +4
elif answer ==3:
    Ravenclaw = Ravenclaw +4
elif answer ==4 :
    Gryffindor = Gryffindor +4
else:
    print('Wrong input')
print()
print()
# đáp án #
if Hufflepuff >= Slytherin >= Ravenclaw >= Gryffindor :
  print("you are Hufflepuff")
elif Hufflepuff <= Slytherin <= Ravenclaw <= Gryffindor :
  print("you are Gryffindor")
elif Slytherin >= Hufflepuff >= Ravenclaw >= Gryffindor :
  print('you are Slytherin')
else:
  print('you are Ravenclaw')
print()
print()