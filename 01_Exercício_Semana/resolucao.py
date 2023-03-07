def euler():
    eps = 0.001
    t = 2.0
    i = 2
    
    
    while True:
        tprev = t
        
        t = pow(1.0 + (1.0 / i), i);
        
        if (fabs(tprev - t) < eps):
             break
        i=i+1
    

euler()