def findnested(nestedDict,inputkey):
    global tracecount
    global dictlength
    outDict={}
    for k in nestedDict.keys():
        if inputkey != k:
            if tracecount == dictlength-1:
                print("inputKey ****: "+ inputkey + " *** do not exist")
                return 0
            outDict=dict(nestedDict.get(k))
            tracecount +=1
            findnested(outDict,inputkey)
        else:
            print("The value for the input key is: "+ str(nestedDict.get(k)) )
            
myDict= {"a":{"b":{"c":"d"}}}
tracecount=0
dictlength = str(myDict).count(":")
findnested(myDict,'c')

