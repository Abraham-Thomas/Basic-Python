filename = './test_files/pi_million_digits.txt'

with open(filename) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  pi_string += line.strip()
  
while True:
  birthday = input("Enter your birthday, in the form mmddyy: ")
  if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
  elif birthday == 'q':
    break
  else:
    print("Your birthday dose not appear in the first million digits of pi")

