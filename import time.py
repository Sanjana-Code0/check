import time 

st=time.time()

for i in range(1000):
    print(i,end='')

et=time.time()

print('Time taken:',et-st)