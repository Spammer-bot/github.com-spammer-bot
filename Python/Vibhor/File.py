file = open("File.txt","r")
data = file.read()
print(data)
file.close()

file = open("File.txt",'w')
file.write("How are you doing\n")
file.write("I am completely fine\n")
file.close()

file = open("File.txt","r")
data = file.read()
print(data)
file.close()

file = open("File.txt","a")
file.write("What is the statusof the python program?\n")
file.write("Thw project is going great.\n")
file.close()

file = open("File.txt","r")
data = file.read()
print(data)
file.close()