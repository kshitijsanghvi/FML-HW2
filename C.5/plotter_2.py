import matplotlib


import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

mean_values = []
mean_plus_std_values = []
mean_minus_std_values = []


cross_output = genfromtxt('output', delimiter=',')
total_sv_list = cross_output[:,:-1]
cross_output = cross_output[:,-1]
deg = [];
for i in range(4):
    deg.append(i+1)
    


pred_output = genfromtxt('pred_output', delimiter=',')
deg = [];
for i in range(4):
    deg.append(i+1)
    

t_sv = []
avg_t_sv = []
f_sv = []
avg_f_sv = []
for i in range(4):
    counter = 0
    while(counter<len(total_sv_list[i])):
        t_sv.append(total_sv_list[i][counter])
        counter+=1
        f_sv.append(total_sv_list[i][counter])
        counter+=1
    avg_t_sv.append(np.mean(t_sv))
    avg_f_sv.append(np.mean(f_sv))
    t_sv = []
    f_sv = []
    
fig, axs = plt.subplots(2, 1,squeeze=False,figsize=(10,10))
axs[0,0].plot(deg,pred_output[:4],'m-',label='Test Error')
axs[0,0].plot(deg,cross_output[:4],'k-',label='Cross Validation Error')
axs[0,0].set(xlabel='Degree',ylabel='Error')
# axs[0,0].ylabel('Error')
axs[0,0].legend()
# axs[0].title('Error vs Degree')

axs[1,0].plot(deg,avg_t_sv,'m-',label='Total SV')
axs[1,0].plot(deg,avg_f_sv,'k-',label='On Margin SV')
axs[1,0].set(xlabel='Degree',ylabel='SV count')
axs[1,0].legend()



matplotlib.pyplot.show()

plt.plot(deg,avg_f_sv,'m-',label='On Margin SV',)
plt.xlabel('Degree')
plt.ylabel('Free SV')
plt.legend()
plt.show();


    

matplotlib.pyplot.show()
