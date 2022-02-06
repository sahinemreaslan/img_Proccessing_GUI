import onisleme
import numpy as np
mask = np.array([[0,255,0],[255,0,255],[0,0,255]])
mask_two = [[255,255,255],[255,255,255],[255,255,255]]
mask_two = [[255,0,255],[0,0,0],[255,0,255]]
def genisletme(img,img_x,img_y):
    img = onisleme.graytobw(img,30,img_x,img_y)
    tut = img
    for i in range(0,img_x,3):
        for j in range(0,img_y,3):
            if img[i][j] == 0 and i-1 > 0 and j-1 >0 and j+1!=img_y and i+1!=img_x:
                tut[i][j-1] = 0
                tut[i+1][j] = 0
                tut[i-1][j] = 0
                tut[i-1][j+1] = 0
    return tut

def erozyon(img,img_x,img_y):
    img = onisleme.graytobw(img,42,img_x,img_y)
    tut = img
    for i in range(0,img_x):
        for j in range(0,img_y):
            if img[i][j] == 0 and i-1 > 0 and j-1 >0 and j+1!=img_y and i+1!=img_x:
                print(img[i-1:i+1][j-1:j+1] == mask_two)
                if img[i-1:i+1][j-1:j+1] == mask_two:
                    tut[i][j-1] = 255
                    tut[i+1][j] = 255
                    tut[i-1][j] = 255
                    tut[i-1][j+1] = 255
    return tut
                            
def cikarma():
    pass