def getHammingDistance(str1, str2):
    #compare size of str1 and str2
    if(len(str1) == len(str2)):
        c = zip(str1,str2)
        d=0;
        for s1,s2 in c:
            if s1!=s2:
                d=d+1

        return d

    else:
        print "Error! Strings are not equal!"
  
