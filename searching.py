list=[20,30,59,80,48]
n=80
pos=-1
def search(list,n):
    count=0
    for count in list:
        if count==n:
            globals()['pos']=list.index(count)+1 #for finding the location
            return True
    return False

if search(list,n):
    print("element found",pos)   #for printing the message
else:
    print("element not found")