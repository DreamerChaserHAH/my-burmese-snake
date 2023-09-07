# Indentation are IMPORTANT
# 4 spaces per tab
# Spaces can confuse python so don't use them in places other than strings!
x = 10
y = 5
if x + y > 10:
    print("Greater than 10")
    if x + y < 20:
        print ("But less than 20")
    elif x + y == 20:
        print ("is 20!")
    else:
        print ("But equal to or more than 20?? wow")
        if(x + y > 25):
            print("much greater than 25!")
else:
    print("nah stucked below 10")