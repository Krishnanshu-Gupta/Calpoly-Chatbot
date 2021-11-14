entered = input("enter: ")

with open('ratemyprofs.txt','r') as f:
    lines = f.readlines()

tID=[]
for line in lines:
    rmpTeacherDict = eval(line)
    tLastName = rmpTeacherDict['tLname']
    if entered.lower() == rmpTeacherDict['tLname'].lower():
        tID.append(str(rmpTeacherDict['tid']))
        print(f"{entered} id = {tID}")

with open('ratereviews.txt','r') as f:
    lines = f.readlines()

readIn=False
rating=[]

TOKEN="***{{{"
counter=len(tID)
print(f"hehe={tID},counter={counter}")
for line in lines[2:]:
    #print(line)
    #print(f"{line}")
    if line.strip('\n') == TOKEN and counter==0:
        print("TOKEN")
        break
    if line.strip('\n') in tID:
        print("started")
        print(f"tid={tID}")
        counter-=1
        print(f"county={counter}")
        readIn = True
    if readIn:
        rating.append(line.split(','))

print(f"class={rating}")




#for line in lines[0:1]:






