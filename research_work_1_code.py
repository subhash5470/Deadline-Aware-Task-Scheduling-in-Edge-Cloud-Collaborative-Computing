#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

n_mach = int(input("Enter the number of machines:"))
mach = [i for i in range(1, n_mach + 1)]
machines = np.array(mach)
print(machines)

n_tasks = int(input("Enter the number of tasks:"))


# In[2]:


def schedule():
    tasks = []
    j = 1
    while j <= n_tasks:
        t = []
        random_values = np.random.randint(low=1, high=10)
        t.append(j)
        t.append(random_values)
        dead = np.random.randint(low=4, high=25)
        t.append(dead)
        tasks.append(t)
        j = j + 1
    k = 1
    while k in range(1, n_tasks + 1):
        ma = np.random.randint(low=1, high=n_mach)
        tasks[k - 1].append(ma)
        k = k + 1
    return tasks


# In[3]:


def makespan(tasks):
    m = 1
    time = []
    while m <= n_mach:
        n = 0
        ti = 0
        while n < n_tasks:
            if tasks[n][3] == m:
                ti = ti + tasks[n][1]
            n = n + 1
        time.append(ti)
        m = m + 1
    max_time = max(time)
    return max_time


# In[4]:


def tgr(tasks):
    n_tasks = len(tasks)
    n_mach = max(task[3] for task in tasks)  # Calculate maximum machine number from tasks
    m = 1
    tgr = 1e-9  # Set tgr to a very small non-zero value

    while m <= n_mach:
        n = 0
        ti = 0

        while n < n_tasks:
            if tasks[n][3] == m:
                ti = ti + tasks[n][1]
                if tasks[n][2] <= ti:
                    tgr += 1
            n = n + 1

        m = m + 1

    tgr = tgr / n_tasks
    return tgr


# In[5]:


generations = 4
j=1
x_axis=[]
y_axis=[]
tg_yaxis=[]


while j<=generations:
    n_tasks=n_tasks+50
    min_makes=[]
    tg=[]
    x_axis.append(n_tasks)
    
    i = 1
    while i < generations:
        print("Generation:", i)
        current_tasks = schedule()
        print("Schedule:", current_tasks)
        print("Makespan:", makespan(current_tasks))
        min_makes.append(makespan(current_tasks))
        print("tgr:",round(tgr(current_tasks),ndigits=3))
        tg.append(tgr(current_tasks))
        print("-------------------------")
        i = i + 1
    y_axis.append(min(min_makes))
    tg_yaxis.append(max(tg))
    
    j=j+1
    
print(min(min_makes))


# In[6]:


tg_yaxis2=tg_yaxis[::-1]


# In[7]:


generations = 4
j=1
x_axis1=[]
y_axis1=[]
tg_yaxis1=[]

while j<=generations:
    n_mach=n_mach+10
    min_makes1=[]
    tg1=[]
    x_axis1.append(n_mach)
    
    i = 1
    while i < generations:
        
        current_tasks = schedule()
        min_makes1.append(makespan(current_tasks))
        tg1.append(tgr(current_tasks))
        i = i + 1
    y_axis1.append(min(min_makes1))
    tg_yaxis1.append(max(tg1))
    
    j=j+1

tg_yaxis3=tg_yaxis1[::-1]


# In[8]:


dataFrame=pd.DataFrame({'xx':x_axis1,'makespan':y_axis1})
ax=dataFrame.plot(x="xx", y="makespan", kind="bar",color='green')
plt.xlabel("Number of machines", fontsize=20)
plt.ylabel("Makespan", fontsize=20)
ax.tick_params(direction='out', length=6, labelsize = 16,width=2, colors='black')
plt.show()


# In[9]:


dataFrame=pd.DataFrame({'xx':x_axis1,'tgr':tg_yaxis3})
ax=dataFrame.plot(x="xx", y="tgr", kind="bar")
plt.xlabel("Number of machines", fontsize=20)
plt.ylabel("TGR",fontsize=20)
ax.tick_params(direction='out', length=6, labelsize = 16,width=2, colors='black')
plt.show()


# In[10]:


dataFrame=pd.DataFrame({'xx':x_axis,'makespan':y_axis})
ax=dataFrame.plot(x="xx", y="makespan", kind="bar",color='green')
plt.xlabel("Number of tasks",fontsize=20)
plt.ylabel("Makespan",fontsize=20)
ax.tick_params(direction='out', length=6, labelsize = 16,width=2, colors='black')
plt.show()


# In[11]:


dataFrame=pd.DataFrame({'xx':x_axis,'tgr':tg_yaxis2})
ax=dataFrame.plot(x="xx", y="tgr", kind="bar")
plt.xlabel("Number of tasks",fontsize=20)
plt.ylabel("TGR",fontsize=20)
ax.tick_params(direction='out', length=6, labelsize = 16,width=2, colors='black')
plt.show()


# In[ ]:




