import numpy as np
from statistics import multimode

size = int(input())

my_list = list(map(int, input().split())) 

print(round(np.mean(my_list), 1))
print(round(np.median(my_list), 1))
print(min(multimode(my_list))) 
