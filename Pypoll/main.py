#analyze data
#Count the total number of votes cast
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath)as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    votes=0
    csvheader=next(csvreader)

    for row in csvreader:
        if row[0] !="":
            votes +=1

#print(votes)

#list canidates who recieved votes
peoplelist = []
allcandidates = []
dict={}
Khan=0
Correy=0
Li=0
OTooley=0

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)

    for row in csvreader:
       if row[2] not in peoplelist:
           peoplelist.append(row[2])
       allcandidates.append(row[2])
    #print(peoplelist)

    for name in allcandidates:
        if name=="Khan":
            Khan = Khan+1
        elif name=="Correy":
            Correy=Correy+1
        elif name=="Li":
            Li=Li+1
        elif name=="O'Tooley" :
            OTooley=OTooley+1

    Sum=Khan+Correy+Li+OTooley
    #print('khan', Khan/Sum, Khan)
    #print('Correy',Correy/Sum, Correy)
    #print (Sum)

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)

    for row in csvreader:
       if row[2] not in peoplelist:
           peoplelist.append(row[2])
           dict[row[2]]=0
    #dict[row[2]]+=1

pct=[Khan/Sum,Correy/Sum,Li/Sum,OTooley/Sum]
votecount=["Khan","Correy","Li","OTooley"]

Top=zip(pct,votecount)
winner=max(Top)
winner1=winner[1]
#Khanpct=Khan/Sum

f=open("output.txt","w+")
print (" ")
f.write(" " +"\n")  
print("Election Results")
f.write("Election Results" +"\n")
print(f"Total Votes: {votes}")
f.write(f"Total Votes: {votes}" +"\n")
print(f"Khan: {round(Khan/Sum*100,4)} % ({Khan})")
f.write(f"Khan: {round(Khan/Sum*100,4)} % ({Khan})" +"\n")
print(f"Correy: {round(Correy/Sum*100,4)} % ({Correy})")
f.write(f"Correy: {round(Correy/Sum*100,4)} % ({Correy})" +"\n")
print(f"Li: {round(Li/Sum*100,4)} % ({Li})")
f.write(f"Li: {round(Li/Sum*100,4)} % ({Li})" +"\n")
print(f"Khan: {round(OTooley/Sum*100,4)} % ({OTooley})")
f.write(f"Khan: {round(OTooley/Sum*100,4)} % ({OTooley})" +"\n")
print(f"Winner: {winner1}")
f.write(f"Winner: {winner1}" +"\n")
print(f"")
outputtxt=os.path.join("output.txt")


    
    
    
    
    
    
    
    

