####Declare###
import os

##Functions##

#####int main####
list = os.listdir()

for x in list:
  for y in x:
      if(y == "tx"):
          print("found it in:",x)
          os.remove(x)
