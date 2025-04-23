# import cv2
# import numpy as np
# import pytesseract

# from collections import deque

# myconfig = r"--psm 6 --oem 3"

# text = pytesseract.image_to_string(cv2.imread("images/random1.jpg"), config=myconfig)

# with open("extracted_text.txt", "r") as text_file:
#     text_file.write(text)

# print(text)

# def doit() -> None:
#     img = cv2.imread("Black and White Image.jpg")

#     box: str = pytesseract.image_to_data(img)
#     print(pytesseract.image_to_string(img))
#     print(box, '\n')

#     for lineNo, line in enumerate(box.splitlines()):
#         line = line.split()
#         if lineNo != 0 and len(line) == 12:
#             x, y, w, h = map(int, line[6:10]) # explanations in below block
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 1)

#     cv2.imwrite('Black and White Image.jpg', img)
#     cv2.imshow('Detection', img)
#     cv2.waitKey(0)



# def doit1() -> None:
#     # selecting the final img
#     img  = cv2.imread("images/random text3.jpg")
#     grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     adaptive_thrsehold = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blockSize=55, C=4)
#     threshold, black_and_white_img = cv2.threshold(grayImg, 80, 255, cv2.THRESH_BINARY_INV)
#     img = adaptive_thrsehold
    
    
#     text = pytesseract.image_to_string(img)
#     with open("extracted_text1.txt", "w") as text_file:
#         text_file.write(text)

# a = 1
# doit() if a == 0 else doit1()



# with open("Extracted By Me.txt", "r") as text_file:
#     contents = text_file.read()
#     for line in contents.splitlines():
#         print(line)

import matplotlib.pyplot as plt
import numpy as np

x = y = np.linspace(-10, 10, 100)  # x1, y1 are not pointing to the same Array.
xx, yy = np.meshgrid(x, y)
zz = xx**2 + yy**2 # Bottom-Left Corner (-10, -10) => 100 + 100 = 200(the highest point of Z axis)

fig = plt.figure(figsize=(10, 10))

ax3 = fig.add_subplot(1, 1, 1, projection='3d')
p = ax3.plot_surface(xx, yy, zz, cmap='ocean')
fig.colorbar(mappable=p, ax=ax3, location='left')
ax3.set_title("3D view of x**2 + y**2")
ax3.set_xlabel("x", labelpad=10, c='red')
ax3.set_ylabel("y", labelpad=10, c='blue')
ax3.set_zlabel("z", labelpad=10, c='green')
# ax3.view_init(17, -143)
plt.show()