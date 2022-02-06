import cv2
import onisleme
import numpy as np   

def kenar_bul(img,img_x,img_y):
    img = onisleme.rgbtogray(img)
    for i in range(0,img_x-1):
        for j in range(0,img_y-1):
            if i != img_x and j != img_y:
                img[i][j] = abs(img[i][j]-img[i+1][j+1])+abs(img[i][j+1]-img[i+1][j])
                if img[i][j] > 120:
                    img[i][j] = 255
                else:
                    img[i][j] = 0
    return img
def mask_func(val,k,m,islem):
    if(islem == 2):
        min_Val = 255 
        max_Val = 0
        for i in range(0,3,1):
            for j in range(0,3,1):
                for c in range(0,3,1):
                    if val[k+i][m+j][c] < min_Val:
                        min_Val = val[k+i][m+j]
                    #print(val[k+i][m+j])
                    if val[k+i][m+j][c] > max_Val:
                        max_Val = val[k+i][m+j]
    return (max_Val+min_Val)/2



def ortanca_bul(img,m,n):
    liste = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=float)
    print(type(img))
    for i in range(m,3):
        for j in range(n,3):
            for k in range(0,3):
                print(img[i][j][k])
    liste.sort()
    return liste[4]
def ortanca(img,img_x,img_y):
    #3x3 mask 8 bit image
    # img = onisleme.rgbtogray(img)
    for i in range(0,img_x):
        for j in range(0,img_y):
            for k in range(0,3):
                if(i != img_x-3 and j != img_y-3):
                    img[i][j][k] = ortanca_bul(img,i,j)
    return img


# def ortalama_bul(img,i,j):
#     for i in range(m,3):
#         for j in range(n,3):
            
def ortalama(img,img_x,img_y):
    for i in range(0,img_x):
        for j in range(0,img_y):
            if i != img_x-2 and j != img_y-2:
                img[i][j] = ortalama_bul(img,i,j)
    return img

# def 