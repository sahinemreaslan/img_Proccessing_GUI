def rgbtogray(img):
    blue_ch = img[:,:,0]
    red_ch = img[:,:,1]
    green_ch = img[:,:,2]
    img = (blue_ch + red_ch + green_ch)/3
    #img = (img * 255).astype(np.uint8)
    return img
#2
def graytobw(img,thresh,img_x,img_y):
    img = rgbtogray(img)
    for i in range(0,img_x):
        for j in range(0,img_y):
          if img[i][j] >= thresh:
            img[i][j] = 0
          else:
            img[i][j] = 255
    return img
#3
def zinzout():
    pass
#4
def img_cut(x1,x2,y1,y2,img):
    if img.shape[0] == 3:#grayscale or B&W
        for i in range(x1,x2):
            for j in range(y1,y2):
                for k in range(0,3):
                    img[i][j][k] = 0
    else:#RGB
        for i in range(x1,x2,1):
            for j in range(y1,y2,1):
                img[i][j] = 0
    return img
