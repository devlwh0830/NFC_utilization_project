import cv2

img = cv2.imread("info.png") # 이미지 불러오기
cv2.imshow("Please Tag Here", img) # 불러온 이미지를 Lenna라는 이름으로 창 표시.
cv2.resizeWindow(winname='Please Tag Here', width=1000, height=500)
cv2.waitKey() # 키보드 입력이 들어올 때까지 창을 유지