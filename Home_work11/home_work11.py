#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# 1. Определить корни
#
# 2. Найти интервалы, на которых функция возрастает
#
# 3. Найти интервалы, на которых функция убывает
#
# 4. Построить график
#
# 5. Вычислить вершину
#
# 6. Определить промежутки, на котором f > 0
#
# 7. Определить промежутки, на котором f < 0


# In[4]:


import sympy
from sympy import is_decreasing, is_increasing
from sympy.abc import x, y
from sympy import S, Interval, oo


# In[ ]:





# In[ ]:





# 1. Определить корни

# In[2]:


import sympy as sympy
from sympy import N, sqrt
import math
import numpy as np


x = sympy.symbols('x')

ans = sympy.solve (-12.0*x**4-18.0*x**3+5*x**2+10.0*x-30.0)
shrinking = (-1 + sqrt(7), -sqrt(7) - 1)
shrinking = list(map(N, shrinking))
print(shrinking)


# 2. Найти интервалы, на которых функция возрастает

# In[13]:


is_increasing(-12.0*x**4-18.0*x**3+5*x**2+10.0*x-30.0, Interval.open(oo, 0))


# Найти интервалы, на которых функция убывает

# In[15]:


is_decreasing(-12.0*x**4-18.0*x**3+5*x**2+10.0*x-30.0, Interval.open(1, oo))


# In[ ]:





# 4. Построить график

# In[19]:


import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
     return -12 * (x**4) * np.sin(np.cos(x)) - 18.0 * x**3 + 5 * x**2 + 10.0 * x - 30.0
# t2 = np.arange(-100.0, 100.0, 0.02)
t2 = np.arange(-25.0, 25.0, 0.02)
test = f(t2)

plt.figure()
plt.subplot(211)
plt.plot(t2, f(t2), 'r-')
plt.show()


# In[ ]:





#  5. Вычислить вершину

# In[16]:


from sympy import Interval, Symbol, minimum, S
minimum(-12.0*x**4-18.0*x**3+5*x**2+10.0*x-30.0, x, S.Reals)


# 6. Определить промежутки, на котором f > 0
#
# 7. Определить промежутки, на котором f < 0
#

# In[21]:


i = -5
while i < 5:
    res = -12.0*i**4-18.0*i**3+5*i**2+10.0*i-30.0
    print(f'{i:5} - {res}')
    i += 0.25


# In[ ]:



