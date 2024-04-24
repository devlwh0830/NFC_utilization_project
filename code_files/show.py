import os, cv2, glob
import schedule, time
import psutil

def TagSystem(number:str):
    # GIF 파일을 엽니다.
    gif = cv2.VideoCapture(f'C:/Users/user/Desktop/nfc/gifs/{number}.gif')

    # GIF 파일의 모든 프레임을 읽어들입니다.
    frames = []
    while True:
        ret, frame = gif.read()
        if not ret:
            break
        frames.append(frame)

    # 모든 프레임을 화면에 출력합니다.
    for frame in frames:
        cv2.imshow('MAKER SPACE SYSTEM', frame)
        cv2.waitKey(30) 
    
    cv2.destroyAllWindows()