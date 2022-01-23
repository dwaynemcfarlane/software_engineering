#!/usr/bin/env python
# coding: utf-8

# In[86]:



class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self.height
    
    @width.setter
    def width(self, width):
        if width <=0:
            raise ValueError("Width must be positive.")
        else:
            self._width = width
    @height.setter
    def height(self, height):
        if height <0:
            raise ValueError("Height must be a positive number")
        else:
            self._height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    def to_string(self):
        return 'Rectangle: width={}, height={}'.format(self.width, self.height)
    def __repr__(self):
        return 'Rectangle({},{})'.format(self.width, self.height)
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return "Not a Rectangle"


# In[87]:


r1 = Rectangle(10,20)


# In[ ]:


r1.perimeter()


# In[ ]:


str(r1)


# In[ ]:


r1.to_string()


# In[ ]:


str(r1)


# In[ ]:


r1 


# In[ ]:


r1 = Rectangle(10,20)


# In[ ]:


r2 = Rectangle(10,20)


# In[ ]:


r1 is not r2


# In[ ]:


r1 == r2


# In[89]:


r1 is r2


# In[90]:


type(r1)


# In[91]:


r3 = (100)


# In[92]:


r1 == r3


# In[ ]:





# In[ ]:




