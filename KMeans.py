#Jill Mercer

import math
import random
import sys
file = open("iris.data")
sys.stdout=open("output.txt","w") #redirects print to go to file instead of terminal

#Number of Clusters and number of elements
iterations = 0
epsilon = .001
myList = []

#Point object used for the data file, all points start in cluster 0 until changed
class Point:
    def __init__(self, first, second, third, fourth, cluster):
        self.p1 = first
        self.p2 = second
        self.p3 = third
        self.p4 = fourth
        self.c = cluster
        
#Function used to find the Euclidean distance between points
def euclideanDist(x,y):
    temp = math.sqrt(math.pow((x.p1-y.p1),2)+math.pow((x.p2-y.p2),2)+math.pow((x.p3-y.p3),2)+math.pow((x.p4-y.p4),2))
    return temp

#Find the new centers by taking average of points
def redoCenters(numIn1,numIn2):
    temp1 = Point(0,0,0,0,0)
    temp2 = Point(0,0,0,0,0)
    
    for x in range (0, len(myList)):
        if myList[x].c == 1:
            temp1.p1 += myList[x].p1
            temp1.p2 += myList[x].p2
            temp1.p3 += myList[x].p3
            temp1.p4 += myList[x].p4
        else:
            temp2.p1 += myList[x].p1
            temp2.p2 += myList[x].p2
            temp2.p3 += myList[x].p3
            temp2.p4 += myList[x].p4
    center1 = Point((temp1.p1/numIn1),(temp1.p2/numIn1),(temp1.p3/numIn1),(temp1.p4/numIn1),0)
    center2 = Point((temp2.p1/numIn2),(temp2.p2/numIn2),(temp2.p3/numIn2),(temp2.p4/numIn2),0)
    return center1, center2
    
#Read in data
line = file.readline()
while line != "":
    word = line.split(',')
    temp = Point(float(word[0]),float(word[1]),float(word[2]),float(word[3]), 0)
    myList.append(temp)
    line = file.readline()
    

#Start the kMeans by picking 2 random points and declare past centers
rand1 = random.randrange(0,len(myList),2)
rand2 = random.randrange(0,len(myList),2)
while rand2 == rand1:
    rand2 = random.randrange(0,len(myList),2)
center1 = myList[rand1]
center2 = myList[rand2]
pastCenter1 = Point(999,999,999,999,0)
pastCenter2 = Point(999,999,999,999,0)


#Group the clusters until iterations reach 20
while iterations <= 20:
    numIn1 = 0
    numIn2 = 0
    for x in range (0, len(myList)):
        dif1 = euclideanDist(myList[x], center1)
        dif2 = euclideanDist(myList[x], center2)
        centerdif1 = euclideanDist(center1, pastCenter1)
        centerdif2 = euclideanDist(center2, pastCenter2)
        if dif1 > dif2:
            myList[x].c=2
            numIn2 =numIn2+1
        else:
            myList[x].c=1
            numIn1=numIn1+1
    #Breaks if center hasn't changed or iterations reached 20
    if (centerdif1 <= epsilon and centerdif2 <= epsilon):
        break
    print("Number of points in cluster 1: ", str(numIn1))
    print("Center 1 for iteration ", str(iterations), " is ", str(center1.p1), str(center1.p2), str(center1.p3), str(center1.p4))
    print("Number of points in cluster 2: ", str(numIn2))
    print("Center 2 for iteration ", str(iterations), " is ", str(center2.p1), str(center2.p2), str(center2.p3), str(center2.p4), "\n")
    
    pastCenter1 = center1
    pastCenter2 = center2
    center1, center2 = redoCenters(numIn1, numIn2)
    iterations += 1
    
#Output to a file
print("Algorithm finished")
print("In cluster 1 Center is: ", str(center1.p1), str(center1.p2), str(center1.p3), str(center1.p4))
print("Number of points in cluster: ", str(numIn1))
for x in range (0, len(myList)):
    if(myList[x].c == 1):
        print(myList[x].p1, myList[x].p2, myList[x].p3, myList[x].p4)
       

print("\nIn cluster 2 Center is: ", str(center2.p1), str(center2.p2), str(center2.p3), str(center2.p4))
print("Number of points in cluster: ", str(numIn2))
for x in range (0, len(myList)):
    if(myList[x].c == 2):
        print(myList[x].p1, myList[x].p2, myList[x].p3, myList[x].p4)
       
        
sys.stdout.close()
file.close()

#Prints list
#for x in range (0, len(myList)):
  #print (myList[x].c)

  
