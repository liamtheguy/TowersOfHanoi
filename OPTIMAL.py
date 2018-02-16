def optimal(num):
    
    initial = 3
    end = 5
    optimal = 2
    i = 3
    while True:
    
        if initial <= num and num <= end:

            return optimal

        else:
            
            optimal += 1
            initial += i
            end += i+1
            i +=1 

        
    
