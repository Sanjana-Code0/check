import time 

st=time.time()

for i in range(100000):
    print(i,end='')

et=time.time()

print('Time taken:',et-st)