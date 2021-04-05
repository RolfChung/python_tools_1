# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:48:58 2021

@author: gamarandor
"""
def traveltime_ls(d):
    """traveltime in seconds with 
    light speed over a distance d"""
    c = 186000  # miles
    
    return d / c

def traveldistance_ls(s):
    """traveldistance in km with 
    light speed given seconds of traveltime"""
    c = 186000  # miles
    return c * s