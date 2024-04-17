####Declare###
import os

##Functions##

#####int main####
while True:
    x = input("Enter a value: ")
    f = open(x, "w")
    f.close()
    if(x == "0"):
        break
    else:
        continue

# for x in list:
#   for y in x:
#       if(y == "1"):
#           print("found it in:",x)
#           os.remove(x)
