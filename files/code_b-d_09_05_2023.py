# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:30:37 2019

@author: Yanan
"""

import numpy as np
import matplotlib.pyplot as plt
'''
Figures of unregulated farmer's optimal strategies.
Based on optimal strategies solved by model, we draw figures in several steps:
    (1) In (b,d,v) cost parameter space, we consider every combination of (b,c,d) 
        and then find out the corresponding optimal strategy according to the 
        model optimal solution. Then we categorize points in (b,d,v) spcace 
        by their corresponding optimal strategies. 
        Since out goal is to present optimal strategies on b-d plane, we can 
        treat veterinary service cost as a fixed parameter.
        
        
        
        
        (1-1) define a rule to categrize points on b-d plane.These are exact 
        conditions we drived from optimization problem.
'''
c,p,beta,l1,l2,l3,v=1000,0.3,0.5,50,250,300,400  #v=170,220,310,400

def color(b,d):
    if b<=l2-l1:
        if v<=l3-l2+c*p:
            if d<=(1-beta)*(l3+b+c*p-l2-v) and d<=beta*v: #lightskyblue [Test,NC,C,Tr, NTr]
                return "Te2"
            elif d>(1-beta)*(l3+b+c*p-l2-v) and b<=l2-l3-c*p+v/(1-beta): #wheat [Not test, not call, Tr]
                return "NTC2"
            elif b> l2-l3-c*p+v/(1-beta) and d> beta*v: #lightcoral [Call,Tr, NTr]
                return "C1"
        elif v>l3-l2+c*p:
            if d<= (1-beta)*b: #green [Test,Tr,NTr]
                return "Te3"
            elif d> (1-beta)*b: #Yellow [Not test, not call,Tr]
                return "NTC2"
    elif b>l2-l1 and b<=beta*(l3-l1+c*p):
        if v<=l3-l2+c*p:
            if b<=l2-l1+v:
                if d<=beta*(l2-l1-b+v) and d<= (1-beta)*(l3+b+c*p-l2-v):
                    return "Te2"
                elif d>(1-beta)*(l3+b+c*p-l2-v) and b<=v-beta*l1-(1-beta)*(l3+c*p)+l2:
                    return "NTC2"
                elif d>beta*(l2-l1-b+v) and b>v-beta*l1-(1-beta)*(l3+c*p)+l2: #lightgray[C, NTr, NTr]
                    return "C2"
            elif b>l2-l1+v:
                return "C2"
        elif v>l3-l2+c*p:
            if d<=(1-beta)*b:
                return "Te3"
            elif d>(1-beta)*b:
                return "NTC2"
    elif b>beta*(l3-l1+c*p) and b<=l3-l1+c*p:
        if v<=l3-l2+c*p:
            if  b<=l2-l1+v:
                if d<=beta*(l2-l1-b+v):
                    return "Te2"
                elif d>beta*(l2-l1-b+v):
                    return "C2"
            elif b>l2-l1+v:
                return "C2"
        elif v>l3-l2+c*p:
            if   d<= beta*(l3-l1-b+c*p):
                return "Te3"
            elif d> beta*(l3-l1-b+c*p):
                return "NTC1"
    elif b>l3-l1+c*p:
        if v<=l3-l2+c*p:
            return "C2"
        elif v>l3-l2+c*p:
            return "NTC1" 
# label values of function color(b,d)
tc1="Call, treat if 'E', \n not treat if 'I'\n E(A)="r'$\beta$'
tt2="Test, not call but treat if 'E', \n call and not treat if 'I' \n E(A)="r'$\beta$'
tc2="Call, never treat \n E(A)=0"
tn2="Neither call nor test,\n always treat \n E(A)=1"
tt3="Test, Never call, \n treat if 'E' and not treat if 'I'\n E(A)="r'$\beta$'
tn1="Neither call nor test,\n never treat \n E(A)=0"
tt1="Test, call and treat if 'E', \n not call and not treat if 'I'\n E(A)="r'$\beta$'

        
'''
        (1-2) In theory, we consider every points in (b,d,v) space. In practice, 
        we consider points that evenly spread one the plane. As long as the 
        distance between every two points are close enough, we can tell when
        the optimal strategy changes. 
'''        

# We consider the points in (0,600) range on b-axis and in (0,200) range on d-axis. 
# The distance between two points in b-axis and d-axis directions is assumed to 
# be 1 and 0.5 respectively. we picked these values since it is appropriate for 
# presenting main findings.
# We can expand or contract the ranges. We can choose smaller distance, then it 
# cost more time to draw colors.
b = np.arange(0,600,1) 
d = np.arange(0,200,0.5)

'''
        (1-3) The following step categorize points by Function color(b,d)
'''        
area = [[x,y] for x in b for y in d] 
area_t2 = [a for a in area if color(a[0],a[1]) == "Te2"]
area_t3 = [a for a in area if color(a[0],a[1]) == "Te3"]
area_c1 = [a for a in area if color(a[0],a[1]) == "C1"] 
area_c2 = [a for a in area if color(a[0],a[1])=="C2"]
area_n1 = [a for a in area if color(a[0],a[1]) == "NTC1"] 
area_n2 = [a for a in area if color(a[0],a[1])=="NTC2"]



'''
    (2) When we draw b-d plane by holding parameter v fixed, we can colored
        points according to their categories.
'''   
# set the size of the figure
fig=plt.figure(figsize=(15,7))
ax1=fig.add_subplot(111) 
# colored each area
plt.xlabel('Antibiotic cost b', fontsize='25')
plt.ylabel('Test cost d', fontsize='25')
ax1.scatter([a[0] for a in area_t2],[a[1] for a in area_t2],c='lightskyblue',linewidths=3,marker='.',alpha = 0.05) #label='Te,NC,C,Tr,NTr'
ax1.scatter([a[0] for a in area_n2],[a[1] for a in area_n2],c='wheat',linewidths=3,marker='.',alpha = 0.05)# label='NTC,Tr')
ax1.scatter([a[0] for a in area_c1],[a[1] for a in area_c1],c='lightcoral',linewidths=3,marker='.', alpha = 0.05) #label='C,Tr,NTr'
ax1.scatter([a[0] for a in area_c2],[a[1] for a in area_c2],c='lightgray',linewidths=3,marker='.',alpha = 0.05) # label='C,NTr,NTr')
ax1.scatter([a[0] for a in area_t3],[a[1] for a in area_t3],c='darkseagreen',linewidths=3,marker='.',alpha = 0.05)#, label='Test,NC,NC,Tr,NTr'
ax1.scatter([a[0] for a in area_n1],[a[1] for a in area_n1],c='tab:brown',linewidths=3,marker='.',alpha = 0.05)#, label='NTC,NTr'
'''       
    (3) To double-check the colored area present optimal strategies correctly,
        we draw indifferent conditions on b-d plane. Indifferent conditions are 
        conditions under which the farmer's optimal strategy switch from one to 
        another. Then we find that in some cases the boundaries of colored areas
        and indifferent conditions coincide, while in some cases indifferent
        conditions go across areas in the same color. That means graphical 
        presentation is more concise.
        You will notice some lines are removed. Those lines go across colored area 
        and are redudant. We remove the lines for conciseness.        
'''
if v<l3-l2+c*p:
    d1=(1-beta)*(l3+b+c*p-l2-v) 
    d2=0*b+beta*v
    d3=beta*(l2-l1-b+v)

    b1=(l2-l1)+0*d
    b2=(l2-l3-c*p+v/(1-beta))+0*d
    b3=(beta*(l3-l1+c*p))+0*d
    b4=(l3-l1+c*p)+0*d 
    b5=(l2-l1+v)+0*d
    b6=(v-beta*l1-(1-beta)*(l3+c*p)+l2)+0*d
 
    
    if v<(1-beta)*(l3-l2+c*p):
        #ax1.plot(b,d1, 'g--', label=r'$d=(1-\beta)*(l_3+b+c*p-l_2-v)$')
        ax1.plot(b[np.where(b<b1[0])],d2[np.where(b<b1[0])], 'r--', label=r'$d=\beta*v$')
        ax1.plot(b[np.where(b>b1[0])],d3[np.where(b>b1[0])], 'b--', label=r'$d=\beta*(l_2-l_1-b+v)$')
        ax1.plot(b1[np.where(d>d2[0])],d[np.where(d>d2[0])], 'g-', label=r'$b=l_2-l_1$')
        #ax1.plot(b2,d, 'r-', label=r'$b=l_2-l_3-c*p+v/(1-\beta)$')
        #ax1.plot(b3,d, 'b-', label=r'$b=\beta*(l_3-l_1+c*p)$')
        #ax1.plot(b4,d, 'y-', label=r'$b=l_3-l_1+c*p$')
        #ax1.plot(b5,d, 'k-', label=r'$b=l_2-l_1+v$')
        #ax1.plot(b6,d, 'm-', label=r'$b=v-\beta*l_1-(1-\beta)*(l_3+c*p)+l_2$')
        ax1.text(80, 120, tc1, horizontalalignment='center', fontsize=15)
        ax1.text(100, 15, tt2, horizontalalignment='center', fontsize=15)
        ax1.text(320, 100, tc2, horizontalalignment='center', fontsize=15)
    elif v>(1-beta)*(l3-l2+c*p) and v<(1-beta)*(l3-l1+c*p):
        ax1.plot(b[np.where(b<b2[0])],d1[np.where(b<b2[0])], 'g--', label=r'$d=(1-\beta)*(l_3+b+c*p-l_2-v)$')
        ax1.plot(b[np.where((b>b2[0]) & (b<b1[0]))],d2[np.where((b>b2[0]) & (b<b1[0]))], 'r--', label=r'$d=\beta*v$')
        ax1.plot(b[np.where(b>b1[0])],d3[np.where(b>b1[0])], 'b--', label=r'$d=\beta*(l_2-l_1-b+v)$')
        ax1.plot(b1[np.where(d>d2[0])],d[np.where(d>d2[0])], 'g-', label=r'$b=l_2-l_1$')
        ax1.plot(b2[np.where(d>d2[0])],d[np.where(d>d2[0])], 'r-', label=r'$b=l_2-l_3-c*p+v/(1-\beta)$')
        #ax1.plot(b3,d, 'b-', label=r'$b=\beta*(l_3-l_1+c*p)$')
        #ax1.plot(b4,d, 'y-', label=r'$b=l_3-l_1+c*p$')
        #ax1.plot(b5,d, 'k-', label=r'$b=l_2-l_1+v$')
        #ax1.plot(b6,d, 'm-', label=r'$b=v-\beta*l_1-(1-\beta)*(l_3+c*p)+l_2$')
        ax1.text(150, 120, tc1, horizontalalignment='center', fontsize=15)
        ax1.text(120, 30, tt2, horizontalalignment='center', fontsize=15)
        ax1.text(330, 100, tc2, horizontalalignment='center', fontsize=15)
        ax1.text(50, 120, tn2, horizontalalignment='center', fontsize=15,rotation=45)
    elif v>(1-beta)*(l3-l1+c*p):
        ax1.plot(b[np.where(b<b6[0])],d1[np.where(b<b6[0])], 'g--', label=r'$d=(1-\beta)*(l_3+b+c*p-l_2-v)$')
        ax1.plot(b[np.where(b>b6[0])],d3[np.where(b>b6[0])], 'b--', label=r'$d=\beta*(l_2-l_1-b+v)$')
        d_in1=(1-beta)*(l3+b6[0]+c*p-l2-v)
        ax1.plot(b6[np.where(d>d_in1)],d[np.where(d>d_in1)], 'm-', label=r'$b=v-\beta*l_1-(1-\beta)*(l_3+c*p)+l_2$')
        
        #ax1.plot(b,d2, 'r--', label=r'$d=\beta*v$')
        #ax1.plot(b1,d, 'g-', label=r'$b=l_2-l_1$')
        #ax1.plot(b2,d, 'r-', label=r'$b=l_2-l_3-c*p+v/(1-\beta)$')
        #ax1.plot(b3,d, 'b-', label=r'$b=\beta*(l_3-l_1+c*p)$')
        #ax1.plot(b4,d, 'y-', label=r'$b=l_3-l_1+c*p$')
        #ax1.plot(b5,d, 'k-', label=r'$b=l_2-l_1+v$')
        
        ax1.text(200, 15, tt2, horizontalalignment='center', fontsize=15)
        ax1.text(400, 100, tc2, horizontalalignment='center', fontsize=15)
        ax1.text(70, 100, tn2, horizontalalignment='center', fontsize=15)
elif v>l3-l2+c*p:
    d1=0*b+v-(1-beta)*(l3+c*p-l2) 
    d2=(1-beta)*b
    
    d4=beta*(l3-l1-b+c*p)

    #b1=(l2-l1)+0*d
    b3=(beta*(l3-l1+c*p))+0*d
    
    
    #ax1.plot(b,d1, 'g--',label=r'$d=v-(1-\beta)*(l_3+c*p-l_2)$')
    ax1.plot(b[np.where(b<b3[0])],d2[np.where(b<b3[0])], 'k-', label=r'$d=(1-\beta)*b$')
    #ax1.plot(b,d3, 'y--', label=r'$d=v-\beta*(l_1+b)-(1-\beta)*(l_3+c*p)+l_2$')
    ax1.plot(b[np.where(b>b3[0])],d4[np.where(b>b3[0])], 'k-', label=r'$d=\beta*(l_3-l_1-b+c*p)$') 
    #ax1.plot(b1,d, 'g-', label=r'$b=(l_2-l_1)$')
    d_in2=beta*(l3-l1-b3[0]+c*p)

    ax1.plot(b3[np.where(d>d_in2)],d[np.where(d>d_in2)], 'k-', label=r'$b=\beta*(l_3-l_1+c*p)$')
    #ax1.plot(b4,d, 'm-', label=r'$b=v-\beta*l_1-(1-\beta)*(l_3+c*p)+l_2$')
    #ax1.plot(b5,d, 'y-', label=r'$b=l_3-l_1+c*p$')
    
    ax1.text(100, 80, tn2, horizontalalignment='center', fontsize=15)
    ax1.text(300, 12, tt3, horizontalalignment='center', fontsize=15)
    ax1.text(500, 80, tn1, horizontalalignment='center', fontsize=15)
'''       
    (3) Last step, we add text about optimal strategies on figures.
        The code is embedded into if conditions above.         
'''

# set the range of axis.
ax1.set_xticklabels([])
ax1.set_yticklabels([])

ax1.set_xlim(0,600)
ax1.set_ylim(0,200)

#The title depends on cost paramters
def title(v):
    if v<=(1-beta)*(l3-l2+c*p):
        return "Farmer's Optimal Decisions When Veterinary Service Cost is Low"
    elif v>(1-beta)*(l3-l2+c*p) and v<=(1-beta)*(l3-l1+c*p):
        return "Farmer's Optimal Decisions When Veterinary Service Cost is Lower Medium"
    elif v>(1-beta)*(l3-l1+c*p) and v<=l3-l2+c*p:
        return "Farmer's Optimal Decisions When Veterinary Service Cost is Upper Medium"
    elif v>l3-l2+c*p:
        return "Farmer's Optimal Decisions When Veterinary Service Cost is High"
# Name the figure depending on cost parameters
cat="NA"
if v<(1-beta)*(l3-l2+c*p):
    cat="Lowv_"
elif v>(1-beta)*(l3-l2+c*p) and v<(1-beta)*(l3-l1+c*p):
    cat="LowerMv_"
elif v>(1-beta)*(l3-l1+c*p) and v<l3-l2+c*p:
    cat="UpperMv_"
elif v>l3-l2+c*p:
    cat="Highv_"
path = 'C:\\Users\\Yanan\\Dropbox\\RA\\First dissertation paper\\Figure\\b-d\\'
plt.savefig(path+cat+'_b-d.png',dpi = 800,bbox_inches = 'tight') 
plt.show()

'''
Note: We do not provide colored verison in formal paper draft. The figures witout 
colors present the same information.
'''