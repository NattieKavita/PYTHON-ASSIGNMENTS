# file read and write

file = open("writefile.txt", "w")
file.write("My name is Natalia Kavita and i love learning")


# error handling lab 

try:
   file = open("myFile.txt","r")
   print(file.read())
except FileNotFoundError:
 print ("Error the file in not found")
finally:
 print("FILE NOT FOUND")


