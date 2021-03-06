import cv2

capture_path = '../media/pedestres.mp4'  # 0 to webcam
BLUE, GREEN, RED = (255, 0, 0), (0, 255, 0), (0, 0, 255)
CYAN, YELLOW = (255, 255, 0), (0, 255, 255)
pos_line, offset = 150, 30
xy1, xy2 = (20, pos_line), (300, pos_line)
area_ret_min = 3000
side_ret_max = 200
jump_on_x_value = 50
cache_detects = []
total = ppl_out = ppl_in = 0
cap = cv2.VideoCapture(capture_path)
fgbg = cv2.createBackgroundSubtractorMOG2()
