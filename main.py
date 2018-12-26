import numpy as np
import matplotlib.pyplot as mplot
from glob import glob

t=0
t2=0
afilenames = glob('a*.txt')
allawords=[]

bfilenames = glob('b*.txt')
allbwords=[]

file=[]

lex={}

neg=0
wneg=0
neu=0
wpos=0
pos=0


for i in range(0,len(afilenames)):
    data=open(afilenames[i], "r")
    data=data.read()
    data=data.replace("\n", " ")
    data=data.replace(".", "")
    data=data.replace("?", "")
    data=data.replace(",", "")
    data=data.replace("!", "")
    data=data.replace("[", "")
    data=data.replace("]", "")
    data=data.replace("(", "")
    data=data.replace(")", "")
    data=data.replace(">", "")
    data=data.replace("<", "")
    data=data.split(" ")
    for j in range(0, len(data)):
        if len(data[j]) > 0:
            if (data[j]) != (data[j].upper()):
                allawords.append(data[j].lower())


for i in range(0,len(bfilenames)):
    data=open(bfilenames[i], "r")
    data=data.read()
    data=data.replace("\n", " ")
    data=data.replace(".", "")
    data=data.replace("?", "")
    data=data.replace(",", "")
    data=data.replace("!", "")
    data=data.replace("[", "")
    data=data.replace("]", "")
    data=data.replace("(", "")
    data=data.replace(")", "")
    data=data.split(" ")
    for j in range(0, len(data)):
        if len(data[j]) > 0:
            if (data[j]) != (data[j].upper()):
                allbwords.append(data[j].lower())

file=open("sentiment_lex.csv", "r")
sent=file.read()
sent=sent.split("\n")


for i in range(0,len(sent)-2):
    sent[i]=sent[i].split(",")
    sent[i][1]= np.float64(sent[i][1])
    lex[sent[i][0]]=sent[i][1]


choice = input("Enter the series name: ")
if choice == "a":
    for i in range(0, len(allawords)):
        if allawords[i] in lex:
            if lex[allawords[i]]>=-1 and lex[allawords[i]]<-.6:
                neg+=1
            if lex[allawords[i]]>=-.6 and lex[allawords[i]]<-.2:
                wneg+=1
            if lex[allawords[i]]>=-.2 and lex[allawords[i]]<=.2:
                neu+=1
            if lex[allawords[i]]>.2 and lex[allawords[i]]<=.6:
                wpos+=1
            if lex[allawords[i]]>.6 and lex[allawords[i]]<=1:
                pos+=1
    
    y = [neg, wneg, neu, wpos, pos]
    y=np.log10(y)
    x = ["Neg", "W.Neg", "Neu", "W.Pos", "Pos"]  
    
    mplot.title("Sentiment Analysis of Series a")
    mplot.xlabel("sentiment")
    mplot.ylabel("log10 Word count")
    mplot.bar(x,y)
    mplot.show()
    
  

elif choice == "b":
    for i in range(0, len(allbwords)):
        if allbwords[i] in lex:
            if lex[allbwords[i]]>=-1 and lex[allbwords[i]]<-.6:
                neg+=1
            if lex[allbwords[i]]>=-.6 and lex[allbwords[i]]<-.2:
                wneg+=1
            if lex[allbwords[i]]>=-.2 and lex[allbwords[i]]<=.2:
                neu+=1
            if lex[allbwords[i]]>.2 and lex[allbwords[i]]<=.6:
                wpos+=1
            if lex[allbwords[i]]>.6 and lex[allbwords[i]]<=1:
                pos+=1
    

    y = [neg, wneg, neu, wpos, pos]
    y=np.log10(y)
    x = ["Neg", "W.Neg", "Neu", "W.Pos", "Pos"]  
    
    mplot.title("Sentiment Analysis of Series b")
    mplot.xlabel("sentiment")
    mplot.ylabel("log10 Word count")
    mplot.bar(x,y)
    mplot.show()
    
    
