import cv2


img = cv2.imread("files/galaxy.jpg", 0)
"""
print(type(img))
print(img)
print(img.shape)
print(img.ndim)
"""
resize_img = cv2.resize(img, (500, 500))
cv2.imshow("picname", resize_img)
cv2.imwrite("galaxy_resized.jpg", resize_img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
