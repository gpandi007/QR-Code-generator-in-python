#!/usr/bin/env python
# coding: utf-8

# In[4]:


import qrcode
sample = qrcode.make("https://www.asktoastrologer.com/")
sample.save("test.jpg")
import cv2
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("test.jpg"))
print(val)


# In[ ]:




