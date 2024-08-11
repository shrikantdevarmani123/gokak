def swaplist(mylist):
    listlen=len(mylist)
    tmp=mylist[0]
    mylist[0]=mylist[-1]
    mylist[-1]=tmp
    print(mylist)
    

mylist=[1,2,3,4,5]
swaplist(mylist)