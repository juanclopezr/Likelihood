import numpy as np

games = 0.
wingb = 0.

for j in range(0,10000):
    line = np.random.random()
    b = 0.
    a = 0.

    for i in range(0,8):
        temp = np.random.random()
        if(temp<=line):
            b+=1.
        else:
            a+=1.
    if(b==3):
        for i in range(0,3):
            temp = np.random.random()
            if(temp<=line):
                b+=1.
            else:
                a+=1.
            print temp<=line
        print b
        if(b==8):
            wingb+=1.
            print 'bob'
        games +=1.
        

prob = wingb/games

print prob
    
