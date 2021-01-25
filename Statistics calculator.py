ListOfNumbers=[]
Dictionary={}
while True:
    Number=input('Input a number\nOr type done to finish\n')
    if Number=='done':
        break
    else:
        try:
            Number=float(Number)
            ListOfNumbers.append(Number)
        except:
            print('I couldn\'t make that a number!')
            continue

while True:
    counter3=0  
    for x in ListOfNumbers:
        if str(x)not in Dictionary.keys():
            Dictionary[str(x)]=1
        else:
            Dictionary[str(x)]+=1
                                                                    #PastX={}
                                                                    #counter3=0
                                                                    #for x in Dictionary:
                                                                      #  if counter3==0:
                                                                      #      PastX=Dictionary[str(x)]
                                                                       # if PastX>Dictionary[str(x)]:
                                                                        #    Dictionary.pop(str(x))
                                                                       #     print(Dictionary)
                                                                       # else:
                                                                        #    PastX=Dictionary[str(x)]
    


    ListOfNumbers.sort()
    counter=0
    CopyOfList=ListOfNumbers[:]
    for x in CopyOfList:
        CopyOfList[counter]=str(x)
        counter+=1
    stringList=', '.join(CopyOfList)
    print('\nThis is how many data points you have:',len(ListOfNumbers))
    print('Sorted list:',stringList)
    length=len(ListOfNumbers)
    Mean=sum(ListOfNumbers)
    Mean=Mean/length
    print('This is the mean:',Mean)
    Difference=[]
    for y in ListOfNumbers:
        MadDifference=y-Mean
        MadDifference=abs(MadDifference)
        Difference.append(MadDifference)
    MAD=sum(Difference)
    MAD=MAD/length
    print("This is the Mean Absolute Deviation (MAD):",MAD)
    
    #These are to find the median
    if length%2!=0:
        OddMedian=length/2
        print('This is the median:',ListOfNumbers[int(OddMedian)])
        (Q1)=length*0.25
        if Q1!=int(Q1):
            LowerQ1=int(Q1)
            HigherQ1=int(Q1)+1
            Q1=(ListOfNumbers[HigherQ1]+ListOfNumbers[LowerQ1])/2
        Q3=length*0.75
        if Q3!=int(Q3):
            try:
                LowerQ3=int(Q3)
                HigherQ3=int(Q3)+1
                Q3=(ListOfNumbers[HigherQ3]+ListOfNumbers[LowerQ3])/2
            except:
                break

    elif length%2==0:
        LowerIndex=length//2-1
        HigherIndex=length//2
        NumberFromLowerIndex=ListOfNumbers[LowerIndex]
        NumberFromHigherIndex=ListOfNumbers[HigherIndex]
        Sum=NumberFromLowerIndex+NumberFromHigherIndex
        EvenMedian=float(Sum)/2
        print('This is the median:',EvenMedian)
        if len(ListOfNumbers)<4:
            break
        Q1=length*0.25
        if Q1!=int(Q1):
            LowerQ1=int(Q1)
            HigherQ1=int(Q1)+1
            Q1=(ListOfNumbers[HigherQ1]+ListOfNumbers[LowerQ1])/2
        Q3=length*0.75
        if Q3!=int(Q3):
            LowerQ3=int(Q3)
            HigherQ3=int(Q3)+1
            Q3=(ListOfNumbers[abs(HigherQ3)]+ListOfNumbers[abs(LowerQ3)])/2
    counter4=0
    Greatest=max(Dictionary.values())
    print('This is the mode:',end=' ')
    for key,value in Dictionary.items():
        counter4+=1   
        if value==Greatest:
            if counter4==len(Dictionary)-1:
                print(key)
            else:
                print(key,end=', ')
        
    
    if isinstance(Q1,float)and isinstance(Q3,float):
        IQR=Q3-Q1
    else:
        IQR=ListOfNumbers[Q3]-ListOfNumbers[Q1]
    print('This is the IQR:',IQR)
    
    #USE IQR REPLACE
    LowerOutlier=[]
    HigherOutlier=[]
    LowerComparison=Q1-IQR*1.5
    HigherComparison=Q3+IQR*1.5
    for x in ListOfNumbers:
        if x<LowerComparison:
            LowerOutlier.append(x)
        elif x>HigherComparison:
            HigherOutlier.append(x)
    counter1=0
    counter2=0
    if len(LowerOutlier)>0:

        for x in LowerOutlier:
            LowerOutlier[counter1]=str(x)
            counter1+=1
        LowerOutlier=', '.join(LowerOutlier)
    elif len(HigherOutlier)>0:
        for x in HigherOutlier:
            HigherOutlier[counter2]=str(x)
            counter2+=1
        HigherOutlier=', '.join(HigherOutlier)
    
    

    if len(LowerOutlier)>0:
        print('These are the lowest outliers:',LowerOutlier)
    if len(HigherOutlier)>0:
        print('These are the highest outleirs:',HigherOutlier)
    break
    
