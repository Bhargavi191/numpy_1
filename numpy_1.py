#!/usr/bin/env python
# coding: utf-8

# ### 1)

# In[2]:


# 5 dimensional array with all zeros and ones


import numpy as np


# In[17]:


a = np.random.randint(2,size=(5,5)) 
b = np.zeros((1,1,1,5,5),dtype=int)
b[0,0,0,:,:]=a
print(b)


# ### 2)

# In[19]:


x= np.zeros([10],dtype=int)
y= np.ones([10],dtype=int)
z= np.full([10],5,dtype=int)
u= np.vstack((x,y,z))



# In[20]:


u


# ### 3)

# In[21]:


x=np.arange(10,22).reshape(3,4)
x


# ### 4)

# In[28]:


np.diag([0,1,2,3,4,5,6,7,8,9])


# ### 5)

# In[23]:


y = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
np.flip(y,0)


# ### 6)

# In[24]:


a = np.array([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])
np.flip(a)


# ### 7)

# In[32]:


a = np.arange(1,101).reshape(10,10)
b = []
for i in a:
    for s in i:
        if s>30 and s<80 and s%5==0:
            b.append(s)
print(a)

print("\nelements grater than 30,less than 80 and multiple of 5 are:")
print(b)


# ### 8)

# In[49]:


v = np.ones((4,4),dtype=int)
v[1:-1,1:-1]=0


# In[50]:


v


# ### 9)

# In[55]:


r = int(input("enter a rows: "))
c = int(input("enter a columns: "))
z = np.zeros((r,c),dtype=int)
for i in range(r):
    for j in range(c):
        if (i+j)%2==0:
            z[i,j]=1
print(z)


# ### 10)

# In[56]:


x = np.array([10,20,30,40])
y = np.array([10,50,20,60])
z = np.intersect1d(x,y)


# In[57]:


z


# ### 11)

# In[62]:


c1 = np.array([[1,2,3],[4,5,6]])
c2 = c1.reshape(-1)
print("original array")
print(c1)
print("reshaped array",c2)


# ### 12)

# In[63]:


a = []
for i in range(0,11):
    a.append(i)
print(a)


# In[ ]:





# In[ ]:




