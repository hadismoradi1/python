import cv2

image = cv2.imread("E:\project\image\input.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

inverted = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

inverted_blurred = cv2.bitwise_not(blurred)
sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("Original", image)
cv2.imshow("Sketch", sketch)

cv2.imwrite("output_sketch", sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()