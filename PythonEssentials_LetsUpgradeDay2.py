#!/usr/bin/env python
# coding: utf-8

# In[7]:


# BAck Slash used to continue line
print("Hello     Python")


# In[12]:


# """ """ Triple
# 1. To use Text Art 
print(""" ab
          bc""")
# 2. Document String  
"""Documneted"""
# 3. Make SQL Queries 
""" Query """

# Escape Sequence same as java


# In[22]:


# Formated Output
name = "XYZ"
marks = 90.62
age = 20
print("The name of person is ", name, "Marks is ", marks, "Age is ", age)

print("The name of person is %s name marks is %10.2f marks and Age is %5d age" %(name, marks, age))


# In[24]:


print(f"The name of person is {name} marks is {marks} and Age is {age}")


# In[39]:


# Python Variables
_10= 20
id(_10)
_20=20
id(_20)


# In[44]:


# power symbol **
print(5 ** 2)

# Division symbol /
# In python3 int/int gives float value and in Python2 it gives int
print(10/3)

#Floor Division : return lowest int value
print(10//3)


# In[49]:


#BitWise Operators
a =240
b = 1
print(bin(a))
print(a|b)
print(a&b)


# In[51]:


# gives error
10 > 9 and 20 > m


# In[52]:


# No error
10 < 9 and 20 > m


# In[58]:


# Membership Operators
# 1. in
# 2. not in
str = "Python Programming"
print("a" in str)
print('x' in str)
print("gram" in str)
print("x" not in str)


# In[65]:


#Identity Operators
a = 10
b = 10
print(a == b)
print(id(a))
print(id(a))
print(a is b)

x = 1.5
y = 1.5
print(x is y)
# if a and b having equal value bet -5 to 256 then they have same memory locations
# otherwise interprete gives different address


# In[ ]:




