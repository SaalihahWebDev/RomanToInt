file=open('Ls 49\Activity 3\Codingal.txt','r')
Counter=0
Content=file.read()
CoList=Content.split("\n")
for i in CoList:
    if i:
        Counter += 1
print("This is a number of lines in a file")
print(Counter)