def getRatings(entered):
    #polyratings section
    startStore=False
    getTeacher=False
    teacher=''
    polyRatings=[]
    messages=[]
    with open('ratemyprofs.txt','r') as f:
        lines = f.readlines()
    for line in lines:
        if "entered" in line.strip("\n"):
            print(line.strip("\n"))
    #return








    #ratemyprofs section

    with open('ratemyprofs.txt','r') as f:
        lines = f.readlines()

    tID=""
    lastNames=[]
    overallRating=""
    diffScore=""
    quality=""
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
                return tID,overallRating
    return "none","none"

def writeReviews(tID):
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
    #print("rating=",rating)

    #print(f"rating={rating[0][10]}")

    feedback=[]
    for clas in rating:
        feedback.append({"Class":clas[10],"Attendance":clas[0],"Clarity":clas[1],"Difficulty":clas[2],"Message":clas[11],"Difficulty Score (out of 5)":clas[14],"Quality Score (out of 5)":clas[19]})
    #print("\n")
    return outputExtended(feedback)

def outputExtended(feedback):
    output=""
    for num,review in enumerate(feedback):
        output+="\n"
        output+=f"Review {num+1}\n"
        for key,value in review.items():
            output+=f"{key}: {value}\n"
    print(output)
    return output

#print(writeReviews("473490"))


#open text file in read mode
