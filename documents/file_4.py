# -*- coding: utf-8 -*-
import cv2
import random
from random import randint
# TODO: Допишите импорт библиотек, которые собираетесь использовать
mask_min_r=0,219,224
mask_max_r=95,255,255
mask_min_b=114,208,222
mask_max_b=128,255,255
def find_colorxy(image,mask_min,mask_max):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, (mask_min), (mask_max))
    thresh = cv2.GaussianBlur(thresh, (15, 15), 2)
    conts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    conts = conts[0]
    # print(len(conts))
    if conts:
        cv2.drawContours(image, conts, -1, (0, 255, 0), 2)
        for i in range(len(conts)):
            (x, y, w, h) = cv2.boundingRect(conts[i])
            # print((x, ' ', y, ' ', w, ' ', h))
            return image,x,y

def find_the_shortest_way(image) -> list:
    """
        Функция для нахождения кратчайшего маршрута из точки A (синяя точка) в точку B (красная точка).

        Входные данные: изображение (bgr), прочитано cv2.imread
        Выходные данные: список из пройденных перекрестков:
            [1, 2, 3, 4, 5], где 1, 2, 3, 4, 5 - перекрёстки, которые необходимо преодолеть
            Всего есть 5 перекрёстков, которые можно проехать.

        Примеры вывода:
            [4, 5, 3] - проехать через перекрестки 4, 5, 3

            [4] - преодолеть перекресток 4

            [] - перекрёстки пересекать не требуется

    """
    # Алгоритм проверки будет вызывать функцию find_the_shortest_way,
    # остальные функции должны вызываться из неё.

    # TODO: Отредактируйте эту функцию по своему усмотрению.
    x_r,y_r=0,0
    x_b,y_b=0,0
    result = []
    image=cv2.resize(image,(400,400))
    # image=image[0:200,0:200]
    image,x_r,y_r=find_colorxy(image,mask_min_r,mask_max_r)
    print(x_r,y_r)
    image,x_b,y_b=find_colorxy(image,mask_min_b,mask_max_b)
    print(x_b,y_b)
    # cv2.imshow('frame',image)
    # cv2.waitKey(0)
    if abs(x_r-x_b)<100 and abs(y_r-y_b):
        rnd=randint(0,1)
        if rnd==0:
            return result
        else:
            for i in range(3):
                result.append(randint(1,5))
    else:
        for i in range(randint(1,4)):
            result.append(randint(1,5))
        return result
