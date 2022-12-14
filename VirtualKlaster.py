# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:22:49 2022

@author: Юрий
"""

import math

TypeKlaster = 1

def Klaster1(path):
    OF = 0
    if path[0]>3: 
        OF=OF+10
    if path[2]==0: 
        OF=OF*5
    if path[4]==0:
        OF=OF+3  
    return OF

def Klaster2(path):
    OF = 0
    OF=OF+path[0]-path[1]+2*path[2]+path[3]+2*path[4]
    OF=OF+0.5*path[5]-0.12*path[6]-path[7]+80*path[8]+0.00001*path[9]
    if path[10]=='Сильное':
        OF=OF+20
    return OF

def Klaster3(path):
    OF = 0
    OF=OF+(path[0]-4)*(path[0]-4)+math.cos(path[1])+math.cos(math.exp(path[2]))+(path[3]-10)*(path[3]-10)+2*path[4]
    OF=OF+0.5*path[5]-0.12*path[6]-path[7]+80*path[8]+0.00001*path[9]
    OF=OF*15
    if path[10]=='Сильное':
        OF=OF+20
    return OF

def Bench4(path):
    a1=path[0]**2
    a2=path[1]**2
    a=1-(a1+a2)**0.5/math.pi
    OF=(math.cos(path[0])*math.cos(path[1])*math.exp((math.fabs(a))))**2
    return OF

def Bench4x(path):
    p0=path[0]+path[1]+path[2]+path[3]
    p1=path[4]+path[5]+path[6]+path[7]
    a1=p0**2
    a2=p1**2
    a=1-(a1+a2)**0.5/math.pi
    OF=(math.cos(p0)*math.cos(p1)*math.exp((math.fabs(a))))**2
    return OF

def Bench4x1(path):
    p0=path[0]+path[1]
    p1=path[2]+path[3]
    a1=p0**2
    a2=p1**2
    a=1-(a1+a2)**0.5/math.pi
    OF=(math.cos(p0)*math.cos(p1)*math.exp((math.fabs(a))))**2
    return OF

def Bench4x2(path):
    p0=path[0]*(path[1]+path[2])
    p1=path[3]*(path[4]+path[5])
    a1=p0**2
    a2=p1**2
    a=1-(a1+a2)**0.5/math.pi
    OF=(math.cos(p0)*math.cos(p1)*math.exp((math.fabs(a))))**2
    return OF

def Bench1(path):
    a1=path[0]**2
    a2=path[1]**2
    a=(a1+a2)/200
    OF=4*math.fabs(math.sin(path[0])*math.cos(path[1])*math.exp(math.fabs(math.cos(a))))
    return OF

def Bench10(path):
    a1=math.sin(path[0])*math.exp((1-math.cos(path[1]))**2)
    a2=math.cos(path[1])*math.exp((1-math.sin(path[0]))**2)
    a=a1+a2
    OF=a+(path[0]-path[1])**2
    return OF

def GetObjectivFunction(path):
    OF=0
    if TypeKlaster==1:
       OF=Klaster1(path)
    if TypeKlaster==2:
       OF=Klaster2(path) 
    if TypeKlaster==3:
       OF=Klaster3(path) 
    if TypeKlaster==401:
       OF=Bench1(path) 
    if TypeKlaster==404:
       OF=Bench4(path) 
    if TypeKlaster==4040:
       OF=Bench4x(path) 
    if TypeKlaster==4041:
       OF=Bench4x1(path) 
    if TypeKlaster==4042:
       OF=Bench4x2(path) 
    if TypeKlaster==410:
       OF=Bench10(path) 
    #print(OF, path)
    return OF
