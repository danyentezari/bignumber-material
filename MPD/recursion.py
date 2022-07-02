def counter(i):
    
    if i <= 10:
        print(i)
        counter(i+1)
    print( "Done", i )
    

counter(1)