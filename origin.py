####Declare Variable###

##Functions##
def increment(y):
    x = int(y)
    x += 1
    return str(x)


#####int main####
f = open("origin_file.txt", "r")
i = f.read()
f.close()
# open for updating
f = open("origin_file.txt", "w")
f.write(x := increment(i))

f.close()
