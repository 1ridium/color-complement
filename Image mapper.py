#!/usr/bin/env python
# coding: utf-8

# In[77]:


import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 5

print 'reading image'
im = Image.open('ibm tape reel.jpg')
outIm = Image.open('frame_fonts.jpg')
im = im.resize((150, 150))      # optional, to reduce time
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

print 'finding clusters'
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
print 'cluster centres:\n', codes

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

index_max = scipy.argmax(counts)                    # find most frequent
peak = codes[index_max]
colour = ''.join(chr(int(c)) for c in peak).encode('hex')
print 'most frequent is %s (#%s)' % (peak, colour)


# In[56]:


invPeak = 255 - peak
invPeak


# In[57]:


outIm


# In[58]:


from skimage import io
import numpy as np


# In[73]:


width, height = outIm.size
new = Image.new('RGB',(width, height), color = 'white')


# In[74]:


outIm.size


# In[75]:


outIm[200, 35]


# In[79]:


pixels = new.load()
oldPixels = outIm.load()


# In[88]:


for i in range(width):
    newR, newG, newB = invPeak
    for j in range(height):
        r, g, b = oldPixels[i,j]
        if(r > 245 and g > 245 and b > 245):
            pixels[i,j] = (255,255,255)
        else: 
            pixels[i,j] = (int(newR), int(newG), int(newB))


# In[89]:


new


# In[ ]:




