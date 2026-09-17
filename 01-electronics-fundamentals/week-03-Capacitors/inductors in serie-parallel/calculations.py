def serie(inductors: None):
    return sum(inductors)
 

def parallel(inductors:None):
    return 1 / sum(1 / c for c in  inductors)



serie([5,5,5])
parallel([5,5,5])