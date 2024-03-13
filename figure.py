#%%
import matplotlib.pyplot as plt
import pandas as pd
import ast
import numpy as np
from sklearn.metrics import r2_score
sample={
    'damp5':14290,
    'damp7':16860,
    'damp9':16960,
    'damp11':17510,
    'damp13':18740,
    'damp15':19310,
    'damp17':19545,
    'damp19':20158,
    'damp21':20878,
    'damp23':21112,
    'damp25':20960,
    'damp11.4':17790,
    'TMD_mass':9.337e4,
    'stiffness':3000
}
data=pd.read_excel('data100.xlsx')
damping=data['params']
point=data['target']
point1=point.values
damping1=damping.to_dict()
TMDmass=[]
for i in range(100):
    mass=damping1[i]
    masss=ast.literal_eval(mass)
    TMDmass.append(masss['TMD_mass'])


dampingbest=damping1[42]
dampingsecond=damping1[43]
damp_data=ast.literal_eval(dampingbest)

damping17=[]
damping17.append(damp_data['damp5'])
damping17.append(damp_data['damp7'])
damping17.append(damp_data['damp9'])
damping17.append(damp_data['damp11'])
damping17.append(damp_data['damp11.4'])
damping17.append(damp_data['damp13'])
damping17.append(damp_data['damp15'])
damping17.append(damp_data['damp17'])
damping17.append(damp_data['damp19'])
damping17.append(damp_data['damp21'])
damping17.append(damp_data['damp23'])
damping17.append(damp_data['damp25'])

damp_data=ast.literal_eval(dampingsecond)

damping32=[]
damping32.append(damp_data['damp5'])
damping32.append(damp_data['damp7'])
damping32.append(damp_data['damp9'])
damping32.append(damp_data['damp11'])
damping32.append(damp_data['damp11.4'])
damping32.append(damp_data['damp13'])
damping32.append(damp_data['damp15'])
damping32.append(damp_data['damp17'])
damping32.append(damp_data['damp19'])
damping32.append(damp_data['damp21'])
damping32.append(damp_data['damp23'])
damping32.append(damp_data['damp25'])
wind=[5,7,9,11,11.4,13,15,17,19,21,23,25]
 
damping_cal=[]
damping_cal.append(sample['damp5'])
damping_cal.append(sample['damp7'])
damping_cal.append(sample['damp9'])
damping_cal.append(sample['damp11'])
damping_cal.append(sample['damp11.4'])
damping_cal.append(sample['damp13'])
damping_cal.append(sample['damp15'])
damping_cal.append(sample['damp17'])
damping_cal.append(sample['damp19'])
damping_cal.append(sample['damp21'])
damping_cal.append(sample['damp23'])
damping_cal.append(sample['damp25'])
figure=plt.figure(1)
# plt.plot(wind,damping17)
# plt.plot(wind,damping_cal)
# plt.plot(wind,damping32)
# plt.xlabel('wind speed(m/s)')
# plt.ylabel('damping(N/(m/s))')
# plt.legend(['best1','calculation','second'])
# plt.savefig('1.png',dpi=600)

plt.figure(2)
plt.scatter(TMDmass,point)
plt.ylim(-1.01,-0.83)
plt.xlabel('TMD mass(kg)')
plt.ylabel('Target')
plt.savefig('point.png',dpi=600)
plt.show()


#co=r2_score(TMDmass,point1)
print(point1)
