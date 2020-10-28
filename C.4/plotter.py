import matplotlib


import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

mean_values = []
mean_plus_std_values = []
mean_minus_std_values = []

for f in range(1,5):
    my_data = genfromtxt('output_'+str(f), delimiter=',')    
    mean = []
    std = []

    for i in range(21):
        mean.append(np.mean(my_data[i]))
        std.append(np.std(my_data[i]))
        
    log_c = []
    for i in range(-10,11):
        log_c.append(i)
        
    
    mean_plus_std = []
    mean_minus_std = []
    
    for i in range(21):
        mean_minus_std.append(mean[i] - std[i])
        mean_plus_std.append(mean[i] + std[i])
    
    mean_values.append(mean)
    mean_plus_std_values.append(mean_plus_std)
    mean_minus_std_values.append(mean_minus_std)
    


fig, axs = plt.subplots(2, 2,squeeze=False,sharex=True,sharey=True,figsize=(10,10))
axs[0, 0].plot(log_c,mean_values[0],'-m',label='Mean')
axs[0, 0].plot(log_c,mean_plus_std_values[0],'k--',label='Mean +- Std')
axs[0, 0].plot(log_c,mean_minus_std_values[0],'k--')
axs[0, 0].set_title('Degree 1')
axs[0, 0].legend()
axs[0, 0].grid()

axs[0, 1].plot(log_c,mean_values[1],'-m')
axs[0, 1].plot(log_c,mean_plus_std_values[1],'k--')
axs[0, 1].plot(log_c,mean_minus_std_values[1],'k--')
axs[0, 1].set_title('Degree 2')
axs[0,1].vlines(6, ymin = 0.15, ymax = 0.5, colors='g', linestyles='dotted', label='Selected Value : 6')
axs[0, 1].legend()
axs[0, 1].grid()

axs[1, 0].plot(log_c,mean_values[2],'-m')
axs[1, 0].plot(log_c,mean_plus_std_values[2],'k--')
axs[1, 0].plot(log_c,mean_minus_std_values[2],'k--')
axs[1, 0].set_title('Degree 3')
axs[1, 0].grid()

axs[1, 1].plot(log_c,mean_values[3],'-m')
axs[1, 1].plot(log_c,mean_plus_std_values[3],'k--')
axs[1, 1].plot(log_c,mean_minus_std_values[3],'k--')
axs[1, 1].set_title('Degree 4')
axs[1, 1].grid()

for ax in axs.flat:
    ax.set(xlabel='Log C', ylabel='Error')

for ax in axs.flat:
    ax.label_outer()
    
fig.suptitle("Error Vs Log C")
matplotlib.pyplot.show()