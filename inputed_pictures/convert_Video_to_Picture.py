#1. copy to folder is input_picture
#2. copy video to folder  input_picture ( File video  Type .MOV) 
#3. open file convert_Video_to_picture
#4. rename defult video = "2"
#5. run convert_Video_to_picture.py
#6. complete
import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('2.MOV')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite("%d.jpg" % count, image)     # save frame as JPEG file
  count += 1
