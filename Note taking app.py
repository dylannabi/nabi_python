#Ask the user whether they want to see notes or #add a note
#If they want to see notes, open the file, read #it, and display the notes
#If they want to add a note, open the file, and append to it what the user says to

#operator = input("see notes or add a note?")
file_name = input("What file would you like to see?")
#print(open(file_name.strip()).read())
# we need to print out the results of opening a file
# then we read and print the result of this

storage = open(file_name.strip()).readlines()
print("The file length is",len(storage))
line_number = input("What line do you want?")
print (storage[int(line_number)- 1])

file = open(file_name, "a")
add_note = input("What do you want to add")
file.write(add_note + "\n")
file.close ()







