# write in file using with()function
with open('file.txt', 'w') as file:
    file.write("Yo... this is my first time in python.")
    file.write("\n")
    file.write("I am learning file handling operations in python.")
    file.close()

    # splitr file into words
    with open('file.txt', 'r') as file:
        data = file.readlines()
        print("Words in this file are...")
        for line in data:
            word = line.split()
            print(word)
            file.close()