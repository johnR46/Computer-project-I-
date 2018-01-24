import cv2
import numpy as np

pic = cv2.imread('frame0.jpg') # ภาพต้นฉบับ
template = cv2.imread('frame0_1.jpg',0) # แม่แบบ
image = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY) # ทำการแปลงสี
result = cv2.matchTemplate(image,template,cv2.TM_CCORR_NORMED) # ทำการจับคู่รูปภาพ
# print(result) # แสดงค่าข้อมูลที่มีความคล้ายกับแม่แบบ
w, h = template.shape[::-1]
loc = np.where(result >= 0.80) # หากรูปที่ตรวจพบมีความคล้ายมากกว่า 83 % (ค่ามากที่สุดคือ 1 คือ 100 %) แล้วจับใส่ numpy

for loc1 in zip(*loc[::-1]):
  cv2.rectangle(pic,loc1,(loc1[0] + w, loc1[1] + h),(0,0,255),1) # ทำกรอบรูปภาพที่คล้ายกับแม่แบบ

cv2.imshow("Result", pic) # แสดงรูปภาพ
cv2.waitKey(0)
