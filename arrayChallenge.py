def ArrayChallenge(strArr): 
    b=strArr[0]
    c=strArr[1].split(',')
    p=[]
    p1=[]
    for i in range(len(c)):
        r=b.split(c[i])
        if len(r)==2:
            k=r[0]+r[1]        
            p.append(k)
    for j in range(len(p)):
        if c.count(p[j])!=0:
            p1.append(p[j])
    strArr=[]
    if p1==[]:
        strArr='not possible'
    else:
        for i in range(len(p1)):
            for j in range(len(p1)):
                n=p1[i]+p1[j]
                if n==b:
                    strArr.append(p1[i])
                    strArr.append(p1[j])
                    strArr=','.join(strArr)
            
    # code goes here 
    return strArr
    
# keep this function call here  
strArrs = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
print(ArrayChallenge(strArrs))