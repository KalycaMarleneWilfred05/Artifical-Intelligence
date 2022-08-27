#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
if __name__ == "__main__":
    n = 9
    print(fibonacci(n))


# In[ ]:




