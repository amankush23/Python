def inte(lst,valid_type):
    return all([valid_type == type(i) for i in lst])
    
        
lst=[234,2354,35,23,5,"aman",23.34]
result=inte(lst,int)
print(result)
