import os
import csv
from pathlib import Path

os.getcwd()
os.chdir('C:/Users/joelw/dataclass/python/Python/PyBank')
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvreader


    count=0
    csvheader=next(csvreader)

    for row in csvreader:
        if row[0] !="":
            count +=1

print(count)

# datasum=sum(csvreader[1])
total=0
net=[]
dates=[]
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvreader


    count=0
    csvheader=next(csvreader)
    for row in csvreader:
        net.append(int(row[1]))
        dates.append(row[0])
    
    for row in net:
        total=total+row
        
        with open(csvpath) as csvfile:
            csvreader=csv.reader(csvfile,delimiter=',')
            csvreader


            count=0
            csvheader=next(csvreader)

            for row in csvreader:
                if row[0] !="":
                    count +=1

    #average= total / count
    print (total)
    print (count)
    #print (average)

changes=[]
for i in range(1,len(net)):
    changes.append(net[i]-net[i-1])

print(len(net))

changesum=0
for row in changes:
        changesum+=row

avg=int(changesum)/int(len(changes))
print (avg)
Months=[]
max=max(changes)
mm=changes.index(max)
print('supposed max date: ',dates[mm+1])
increasedate=dates[mm+1]
#print(mon)
print (max)

min=min(changes)
mm2=changes.index(min)
print('supposed min date: ',dates[mm2+1])
print (min)
decreasedate=dates[mm2+1]

f=open("output.txt","w+")
print (" ")
f.write(" " +"\n")

print(f"Financial Analysis")
f.write("Financial Analysis" +"\n")
print(f"Total Months: {count}")
f.write(f"Total Months: {count}" +"\n")
print(f"Total:  ${total}")
f.write(f"Total: ${total}" +"\n")
print(f"Average  Change: $ {avg}")
f.write(f"Average  Change: $ {avg}" +"\n")
print(f"Greatest Increase in Profits: {increasedate} $ {max}")
f.write(f"Greatest Increase in Profits: {increasedate}  $ {max}" +"\n")
print(f"Greatest Decrease in Profits: {decreasedate} $ {min}")
f.write(f"Greatest Decrease in Profits: {decreasedate} $ {min}" +"\n")
outputtxt=os.path.join("output.txt")
