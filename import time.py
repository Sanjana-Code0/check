import time 

st=time.time()

for i in range(10):
    print(i,end='')

et=time.time()

print('Time taken:',et-st)
