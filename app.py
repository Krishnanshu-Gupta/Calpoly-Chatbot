from os import major
from re import search
from flask import Flask, render_template, request
from chat import getRatings, writeReviews
import json
import pandas as pd

app = Flask(__name__)
currentProf = "2668323"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    query2 = (request.args.get('msg'))
    query = query2.lower()
    if(query == "yes"):
        return writeReviews(currentProf)
    if(query == "no"):
        return "Oh ok, no worries!"
    if(query == "hi" or query == "hey" or query == "hello"):
        return "Hey! Search for a professor, class, or major."
    
    result = majors(query2.strip())
    if result != False:
        return "Here's a link to your major!\n " + result

    result = classes(query2.strip())
    if result != False:
        return "Here's some information about your class!\n " + result

    return searchProfs(query)

def majors(query):
    query
    with open("majors.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if(query in line):
                line = line.strip("\n")
                ind = line.index("<a href=")
                line1 = line[ind:]
                ind2 = line1.index(">")
                line2 = line1[0:ind2]
                #print(line2[9:len(line2) - 1])
                return "https://catalog.calpoly.edu" + line2[9:len(line2) - 1]
    return False

def classes(query):
    text_file = open("major_data.json", "r")
    #read whole file to a string
    data = text_file.read()
    #close file
    text_file.close()   
    print(query + ",")
    try:
        arr = list(query)
        arr[arr.index(" ")] = " "
        query = ''.join(arr)
        ind = data.index(query.strip())
    except:
        return False
    data2 = data[ind - 11:]
    return (data2[0: data2.index("}")])

def searchProfs(query):
    print("djfsd")
    id, rating = getRatings(query)
    if(id == "none" or rating == "N/A"): 
        return "No ratings found ;("
    else:
        print(id)
        currentProf = id
        result = "Oh yea, I know them!\nThe rating I found on Rate My Professor is " + str(rating)
        quest = ". Would you like to get some more information?"
        return result + quest
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=54321)


