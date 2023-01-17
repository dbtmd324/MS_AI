import os
import glob
import cv2
import random
import shutil

# os.makedirs("./dataset/" + "20m", exist_ok=True)
# os.makedirs("./dataset/" + "20w", exist_ok=True)
#
# folder_name_m = "./dataset/" + "20m"
# folder_name_w = "./dataset/" + "20w"
#
# age20 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# age30 = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
# age40 = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
# age50 = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
# age60 = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
# age70 = [70, 71, 72, 73, 74, 75]

#### AAF 데이터 추가 코드 ####

image_list = os.listdir("/Users/won-yooseung/Desktop/5_MS AI/2_이미지 세션/0116/All-Age-Faces Dataset/aglined faces")

print(len(image_list))

exit()

image_list_woman = image_list[:7380]
image_list_man = image_list[7380:]

"""
for i in age20:
    i = str(i)
    path_man = '.\\AFAD-Full\\'+ "{}".format(i) +'\\111'
    path_woman = '.\\AFAD-Full\\' + "{}".format(i) + '\\112'

    for index1, path1 in enumerate(glob.glob(os.path.join(path_man,"*"))):
        image_name1 = path1.split("\\")[-1]
        image_name1 = image_name1.split(".")[0]
        img1 = cv2.imread(path1)
        cv2.imwrite(os.path.join(folder_name_m, image_name1 + ".png"), img1)
    print("남자 끝")
    for index2, path2 in enumerate(glob.glob(os.path.join(path_woman,"*"))):
        image_name2 = path2.split("\\")[-1]
        image_name2 = image_name2.split(".")[0]
        img2 = cv2.imread(path2)
        cv2.imwrite(os.path.join(folder_name_w, image_name2 + ".png"), img2)
    print("여자 끝")
"""
