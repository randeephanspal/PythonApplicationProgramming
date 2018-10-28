import timeit
import matplotlib.pyplot as plt
from collections import Counter

#words.txt contains 100,000 words
f=open('words2.txt','r')
totalWords=(f.readline())
splitWord = totalWords.split()
print("Length of words",(splitWord))

timeList=[]

def wordsInStringToDictWordCount(s):
    dict = {}
    # Split the string in list
    splittedList = s.split()
    # for loop to iterate each element
    for i in splittedList:
        if (i not in dict):
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
    print (dict)

def wordsInStringToDictWordCount(splitWord):
    sum=0
    for i in range(splitWord):
        sum = sum + 1
    return sum
mynumber = 10
mytime = timeit.timeit('wordsInStringToDictWordCount(100000)', 'from __main__ import wordsInStringToDictWordCount', number=10)
computeTimewithoutCounter =(mytime / 10)
timeList.append(computeTimewithoutCounter)
print ("Compute Time without using Counter:",computeTimewithoutCounter)

def wordsInStringToCounter(splitWord):
    counter = collections.Counter(splitWord)
    counterDict={}
    for word in counter:
        counterDict[word]=counter[word]
    print (counterDict)

def wordsInStringToCounter(splitWord):
    sum=0
    for i in range(splitWord):
        sum = sum + 1
    return sum
mynumber = 10
mytime = timeit.timeit('wordsInStringToCounter(100000)', 'from __main__ import wordsInStringToCounter', number=10)
computeTimeCounter=(mytime / 10)
timeList.append(computeTimeCounter)
print ("Compute Time using Counter:",computeTimeCounter)

#Ready to plot
plt.ylabel('Time')
plt.xlabel('Function Name')
plt.title('Comparison Graph\n')
plt.bar(['wordsInStringToDictWordCount','wordsInStringToCounter'],timeList,color="green")
plt.show()