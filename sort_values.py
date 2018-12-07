
def sort_two_values(x):
    
    if type(x) is list:
    
        if len(x) == 2:
       
            for i in range(len(x)):

                if (type(x[i]) != float) or (type(x[i]) != int):
                    print("you didn't give me numbers")

                elif (type(x[i]) is float) or (type(x[i]) is int):

                    if x[0] <= x[1]:
                            print(x)
                    elif x[0] > x[1]:
                            x.sort()
                            print(x)   
        else:
            print("you didn't give me two numbers")
            return none
    else:
        print("you didn't give me a list")
        return none
        
     #                 else:
        #                     print("you didn't give me numbers")

##somehow it loops twice        
