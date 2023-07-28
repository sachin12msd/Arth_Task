import cv2
import numpy as np

width = 400
height = 400
canvas = np.ones((height, width, 3), dtype=np.uint8) * 255

car_color = (0, 0, 255)  # Red
body_top_left = (100, 200)
body_bottom_right = (300, 300)
thickness = -1
cv2.rectangle(canvas, body_top_left, body_bottom_right, car_color, thickness)

window_color = (255, 255, 0)  # Yellow
window_top_left = (140, 220)
window_bottom_right = (180, 260)
cv2.rectangle(canvas, window_top_left, window_bottom_right, window_color, thickness)

window_top_left = (220, 220)
window_bottom_right = (260, 260)
cv2.rectangle(canvas, window_top_left, window_bottom_right, window_color, thickness)
#wheels
wheel_color = (0, 0, 0)  # Black
wheel_center1 = (150, 310)
wheel_radius1 = 30
cv2.circle(canvas, wheel_center1, wheel_radius1, wheel_color, thickness)

wheel_center2 = (250, 310)
wheel_radius2 = 30
cv2.circle(canvas, wheel_center2, wheel_radius2, wheel_color, thickness)

cv2.imshow('Car', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
