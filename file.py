# writing initial data
with open('log.txt','w') as file:
    file.write("log started\n")


# appending entries
with open ('log.txt','a') as file:
    file.write("first even happened\n")
    file.write("second event happened\n")

# reading and printing all entries
with open('log.txt','r') as file:
    print(file.read())