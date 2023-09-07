try:
    cheese = open("cheese.txt", 'r')
    for line in cheese:
        print(line.rstrip())
except:
    print("File cannot be found")
