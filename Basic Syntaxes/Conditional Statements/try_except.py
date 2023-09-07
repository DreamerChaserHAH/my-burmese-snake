# Exception Handling basically
temp = "Fahr 5"
try:
    #This line will throw error because temp has unconvertable characters
    itemp = int(temp)
    print(str(itemp))
except:
    print("OMG! Something happened :((")