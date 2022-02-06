import cv2
import numpy as np
import matplotlib.pyplot as plt
def hist_create(img,img_x,img_y):
    histogram = list(np.zeros(255))
    histogram = [int(histogram) for histogram in histogram]
    #print(img[:,:,-1])
    if img.shape[0] == 3:#grayscale or B&W
        for i in range(0,img_x,1):
            for j in range(0,img_y,1):
                for k in range(0,3):
                    histogram[int(img[i][j][k])] += 1
                
    # else:
    #     for i in range(0,img_x,1):
    #         for j in range(0,img_y,1):
    #             histogram[int(img[i][j])] += 1
    plt.title('GrayScale Histogram - SahinEmre')
    plt.xlabel('Number Of Bits')
    plt.ylabel('0-255 Bit Values')
    plt.hist(histogram)
    plt.savefig("hist.png")
    img = cv2.imread('hist.png')
    return img

#normallestirilmis histogram
def hist_eq(img):
    imgx,imgy,imgch = img.shape
    sumpix = 390*390
# ============================================================================
# histogram olustur
# =============================================================================
    histogram = list(np.zeros(255))
    histogram = [int(histogram) for histogram in histogram]
    #print(img[:,:,-1])
    for i in range(0,224,1):
        for j in range(0,224,1):
            histogram[int(img[i][j])] += 1
    histogram_eq = list(np.zeros(255))
# =============================================================================
# kumulatif dağılım
# pixellerin bulunma olasılığı
# =============================================================================            
    for i in range(0,255,1):    
        for j in range(0,i,1):
            histogram_eq[i] = histogram_eq[i] + histogram[j]
# =============================================================================
# histogram esitleme
# (l-1)*kumulatif dagilim = 254 * histogram_eq
# =============================================================================
    type(histogram_eq)
    donusum_fonk = 253 * histogram_eq
    hist_es_foto = np.zeros_like(sumpix)
    for i,pixel in enumerate(sumpix):
        hist_es_foto[i] = donusum_fonk[pixel]
    hist_es_foto.reshape(sumpix).astype(np.uint8)
    plt.title('GrayScale Histogram - SahinEmre')
    plt.xlabel('Number Of Bits')
    plt.ylabel('0-255 Bit Values')
    plt.hist(hist_es_foto)
    plt.savefig("hist_es_foto.png")
    img = cv2.imread('hist_es_foto.png')
    return img