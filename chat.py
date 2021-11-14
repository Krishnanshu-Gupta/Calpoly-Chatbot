def getRatings(entered):
    with open('ratemyprofs.txt','r') as f:
        lines = f.readlines()

    tID=""
    lastNames=[]
    overallRating=""
    for line in lines:
        rmpTeacherDict = eval(line)
        tLastName = rmpTeacherDict['tLname']
        lastNames.append(tLastName)
        #print(f"lastnames={lastNames}")
        if entered.lower() == rmpTeacherDict['tLname'].lower():
            if tID=="":
                tID = str(rmpTeacherDict['tid'])
                overallRating = rmpTeacherDict['overall_rating']
            #print(f"id={tID}")
            #print(f"{entered} id = {tID}")

    with open('ratereviews2.txt','r') as f:
        lines = f.readlines()

    readIn=False
    done=False
    rating=[]

    TOKEN="***{{{"

    #print(f"hehe={tID},counter={counter}")
    for line in lines[2:]:
        #print(line)
        #print(f"{line}")
        if line.strip('\n') == TOKEN and done:
            #print("TOKEN")
            break
        if line.strip('\n') in tID:
            #print("started")
            #print(f"tid={tID}")
            #print(f"county={counter}")
            done=True
            readIn = True
        if readIn:
            #print(f"splitty={line.split(',')}")
            rating.append(line.split(','))

    rating=rating[1:]
    print("rating=",rating)

    #print(f"rating={rating[0][10]}")

    feedback=[]
    for clas in rating:
        feedback.append({"class":clas[10],"attendance":clas[0],"clarity":clas[1],"difficulty":clas[2],"message":clas[11],"score":overallRating})
    print(feedback)
    return feedback

getRatings("abney")

