import cv2 as cv
import numpy as np

Img_orig = cv.imread('RGB.jpg')

# Перевірка правильності зчитування
cv.imshow('Original Image', Img_orig)
cv.waitKey(0)
cv.destroyAllWindows()

# Окремий канал червоного (R)
Img_r = Img_orig.copy()
Img_r[:, :, (0, 1)] = 0  # обнуляємо канали G і B

# Збереження зображення у форматі JPG з максимальною якістю (100)
cv.imwrite('Surname_Group_Img_R_100.jpg', Img_r, [cv.IMWRITE_JPEG_QUALITY, 100])

# Якщо потрібно зберегти зображення з іншими параметрами
cv.imwrite('Surname_Group_Img_R_10.jpg', Img_r, [cv.IMWRITE_JPEG_QUALITY, 10])
cv.imwrite('Surname_Group_Img_R_50.jpg', Img_r, [cv.IMWRITE_JPEG_QUALITY, 50])
 