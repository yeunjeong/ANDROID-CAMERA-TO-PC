import requests 
import cv2 as cv
import pyvirtualcam
import numpy as np 
import urllib3

urllib3.disable_warnings()

url = "https://10.102.101.161:8080" + "/shot.jpg" 

# 전송되는 영상의 크기와 같아야 한다
# 일단 640*480으로 맞춰두었다.
with pyvirtualcam.Camera(width=640, height=480, fps=20) as cam:
    print(f'Using virtual camera: {cam.device}')
    print("streaming...")
    while True:
        response = requests.get(url, verify=False)
        # print(response)

        arr = np.array(bytearray(response.content),dtype=np.uint8) #converting response to numpy array
        img = cv.imdecode(arr,-1)#decoding numpy array
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        cam.send(img)
        cam.sleep_until_next_frame()
        '''
        cv.imshow("Vivek_Codes", img)# showing image
        if cv.waitKey(1) == 27: #if usr press esc key thn break the while loop
            break
        '''


