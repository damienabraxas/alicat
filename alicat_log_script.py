# -*- coding: utf-8 -*-
"""
Created on Wed Aug 08 10:11:11 2018
This is a script using 

@author: Ryan.Schmitt
"""

from alicat import FlowController
#input Com Port for Serial Communication
flow_controller = FlowController(port='COM3')

#set the setpoint, between 0 and 250 SLPM for our Mass flaw controller

insetpoint=input('Enter the Setpoint between 0 to 250 SLPM(integer value):')
insetpoint=int(insetpoint)
flow_controller._set_setpoint(insetpoint)
#flow_controller.set_flow_rate(insetpoint)


#get time and Setpoint and add it to the file name, file saved as csv
import time
t=time.strftime('%Y_%m_%d_%H_%M_%S')
f =open('mass_flow'+str(insetpoint)+'SLPM_'+t+'.csv', "a")

#file header
f.write('time'+','+'temperature'+','+'mass_flow'+','+'setpoint'+','+'gas'+','+'pressure\r')

#Log Data with time
from time import time

t0=time()

print ("press 'CTRL+C' to quit...") 
with f:
    while True:
        import time
        t=time.strftime('%H_%M_%S')
        time.sleep(1)
        #timestamp = t0+1
        print(t)
        print(flow_controller.get())
        dataDict = flow_controller.get();                          
        logString= str(dataDict['temperature'])+','+ str(dataDict['mass_flow']) +','+str(dataDict['setpoint']) + ',' + str(dataDict['gas']) +','+str(dataDict['pressure'])+'\r'
        f.write((t) + ','+ logString)
#    import msvcrt 
#    char = msvcrt.getch()
#    if char=='q':
#            break
f.close()
 

#ask the user when to quit logging data       
