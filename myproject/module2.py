# -*- coding: utf-8 -*-

# Sum element of a list
def sumup_2(nl):
    s = 0
    for i in nl:
        s += i
    
    return s

# Get the length of a list of numbers
def length_2(nl):
    index = []
    for e,i in enumerate(nl):
        index.append(e)
        
    return index[-1]


# Mean = sum(ni) / length(ni)
def meanup_2(nl):
    return sumup_2(nl) / length_2(nl)

# Median: Median = (n + 1) / 2
def medianup_2(nl):
    m = int((length_2(nl) + 1) / 2)
    
    nls = sorted(nl)
    
    return nls[m]