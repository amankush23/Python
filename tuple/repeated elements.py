t=(2,3,4,25,23,3,4,45,45,45,65)
reg=[]
for i in t:
        if t.count(i) > 1 and i not in reg:
            print(i)
            reg.append(i)
        

