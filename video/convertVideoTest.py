import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('IMG_1317.MOV')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1
