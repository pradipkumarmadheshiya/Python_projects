# matplotlib library, bubble sort

import matplotlib.pyplot as plt
import numpy as np

lst=np.random.randint(0,100,12)
x=np.arange(0,12,1)

n=len(lst)
for i in range(n):
    for j in range(n-i-1):
        plt.bar(x,lst)
        plt.pause(1)
        plt.clf()
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
plt.show()

# matplotlib library, selection sort

# import matplotlib.pyplot as plt
# import numpy as np

# lst=np.random.randint(0,25,9)
# x=np.arange(0,9,1)

# n=len(lst)
# for i in range(n):
#     mn=i
#     for j in range(i+1,n):
#         plt.bar(x,lst)
#         plt.pause(1)
#         plt.clf()
#         if lst[j]<lst[mn]:
#             mn=j
#     lst[mn],lst[i]=lst[i],lst[mn]
# plt.show()