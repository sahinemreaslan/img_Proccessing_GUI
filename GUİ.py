from tkinter import simpledialog as sd #opendialogwindow
from tkinter import filedialog as fd#opendialogwindow
from tkinter import ttk,IntVar
import tkinter as tk
from PIL import Image,ImageTk #ImageTK 
import os,onisleme,onislemeiki,onislemeuc,cv2,onislemedort
#<-----------------FRAME & LOCATİON --------------------->
window = tk.Tk()
window.geometry("1080x540")
window.wm_title("İMG Proccessing Example - 181220027 - Şahin Emre ASLAN")
window.bind("<Escape>",lambda event: window.destroy()) # escape tuşuna basarsa çık
#<-----------------PANE WİNDOW --------------------->
pw = ttk.PanedWindow(window,orient = tk.HORIZONTAL)
pw.pack(fill = tk.BOTH,expand = True)
pw2 = ttk.PanedWindow(pw,orient = tk.VERTICAL)
pw3 = ttk.PanedWindow(pw,orient = tk.VERTICAL)
#<-----------------FRAME & LOCATİON --------------------->
#frame 1 rigth vertical
#frame 2 left header
#frame 3 left footer
frame1 = ttk.Frame(pw,width = 360,height = 540,relief = tk.SUNKEN)
frame2 = ttk.Frame(pw,width = 360,height = 100,relief = tk.SUNKEN)
frame3 = ttk.Frame(pw,width = 360,height = 440,relief = tk.SUNKEN)

pw3.add(frame1)
pw2.add(frame3)
pw2.add(frame2)
pw.add(pw2)
pw.add(pw3)

lbl = tk.Label(frame1)
img = 0
imgtk = 0

global img_x,img_y

#<-----------------Button Function --------------------->
def open_file():
    fln = fd.askopenfilename(initialdir = os.getcwd(),title = "select file", filetypes =(("JPG File","*.jpg"),("PNG file","*.png"),("ALL files","*.*")))
    global img_x,img_y,imgtk,img
    img = cv2.imread(fln)
    #Rearrange colors
    blue,green,red = cv2.split(img)
    img_x,img_y = blue.shape
    img = cv2.merge((red,green,blue))
    ##
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    ##
    lbl.configure(image = imgtk)
    lbl.image = imgtk
    ##
    button_show_image.destroy()
def img_change(img2):
    global img
    img = img2
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    lbl.configure(image=imgtk)
    lbl.image = imgtk


def show_result():
    global img
    if yapim.v.get() == 1:
        if(yapim.combobox1.get()==a[0]):
            img_change(onisleme.rgbtogray(img))
            
        elif(yapim.combobox1.get()==a[1]):
            thresh = sd.askinteger("Input", "Thershold gir: [0-255]",
                    parent=frame2)
            if thresh is not None:
                img_change(onisleme.graytobw(img,thresh,img_x,img_y))
            
        elif(yapim.combobox1.get()==a[3]):
            #kullanıcıya dialog penceresi aç ve değerleri al x,y,z,ch
            #onisleme.init(x,y,z,ch,img)
            x1 = sd.askinteger("Input", "x1 gir:",
                        parent=frame2)
            x2 = sd.askinteger("Input", "x2 gir:",
                       parent=frame2)
            y1 = sd.askinteger("Input", "y1 gir:",
                         parent=frame2)
            y2 = sd.askinteger("Input", "y2 gir:",
                         parent=frame2)
            if (x1 < img_x and x2 < img_x and y1 < img_y and y2 < img_y):
                if x1 and x2 and y1 and y2 is not None:
                    img_change(onisleme.img_cut(x1,x2,y1,y2,img))
                #messaged panel 
        else:
            #don't working
            # this is section zoom in and zoom out sections
            pass
    if yapim2.v.get() == 1:
        for i in range(0,len(b)):
            if yapim2.combobox1.get() == b[i]:
                img_change(onislemeiki.hist_create(img,img_x,img_y))
    if yapim3.v.get() == 1:
        if yapim3.combobox1.get() == c[0]:#gauss bulanik     
            print("debuggg")
        if yapim3.combobox1.get() == c[1]:#keskinlestirme
            pass
        if yapim3.combobox1.get() == c[2]:#kenar bulma           
            img_change(onislemeuc.kenar_bul(img,img_x,img_y))
        if yapim3.combobox1.get() == c[3]:#ortalama        
            img_change(onislemeuc.ortalama(img,img_x,img_y))
        if yapim3.combobox1.get() == c[4]:#ortanca 
            img_change(onislemeuc.ortanca(img,img_x,img_y))
        if yapim3.combobox1.get() == c[4]:#kontra 
            img = onisleme.rgbtogray(img)   
            img_change(onislemeuc.ortanca(img,img_x,img_y))
    if yapim4.v.get() == 1:
        if yapim4.combobox1.get()==d[0]:
            img_change(onislemedort.genisletme(img,img_x,img_y))
        if yapim4.combobox1.get()==d[1]:
            img_change(onislemedort.erozyon(img,img_x,img_y))
btn_show = tk.Button(frame2,text= "<<Sonuçları Göster>>",
                   bg = "black", fg = "white", activeforeground= "black",
                   height = 5, width = 25,command = show_result)
btn_show.place(relx=0.7, rely=0.6)

btn_img_down = tk.Button(frame2,text= "<<İmg Save>>",
                   bg = "black", fg = "white", activeforeground= "black",
                   height = 5, width = 15,command = show_result)
btn_img_down.place(relx= 0.4,rely = 0.6)
    #B.createNewWindow()
    #exit()
    #top = toplevel()
    #top.title("second window")
    #untitled2.button_forward.pack()
#<-----------------LABEL 2 WİDGETS & LOCATİON --------------------->
#button_SHOW_İmage
button_show_image = tk.Button(frame3,text= "İMG Upload !",
                   bg = "black", fg = "white", activeforeground= "black",
                   height = 2, width = 15,command = open_file)
button_show_image.grid(row = 0,column = 0,pady = 12,padx = 20)

class my_struct():
    def method(self):
        if self.v.get() == 1:
            self.combobox1.configure(state="readonly")
        else:
            self.combobox1.configure(state="disabled")
    def check_combo(self):
        return self.combobox1.get()
    def __init__(self,frame3,text1,text2,v,x,c_values):
        self.text1 = text1
        self.text2 = text2
        self.v = v
        self.x = x
        self.frame3 = frame3
        problem = tk.StringVar()
        combobox = ttk.Combobox(frame3,textvariable = problem,values =(c_values),state = "disabled")
        combobox.grid(row = self.x, column = 2,pady = 21,padx = 20)
        self.combobox1 = combobox
        radyo__1 = tk.Radiobutton(frame3, text=self.text1, variable=v, value=1,command=self.method).grid(row = self.x, column = 0,pady = 21,padx = 20)
        self.radyo_1 = radyo__1
        radyo__2 = tk.Radiobutton(frame3, text=self.text2, variable=v, value=2,command=self.method).grid(row = self.x, column = 1,pady = 21,padx = 20)
        self.radyo__2 = radyo__2


v = IntVar(frame3,2)
v1 = IntVar(frame3,2)
v2 = IntVar(frame3,2)
v3 = IntVar(frame3,2)

a = ["RGB_to_GRYSCL","GRYSCL_to_B&W","Zoom_in","Cut"]
yapim = my_struct(frame3,"On_isl.uyg.istiyorum.","On_isl.uyg.istemiyorum",v,1,a)
b = ["Hist_Create","Hist_Eq","Hist_Quant"]
yapim2 = my_struct(frame3,"On_isl.uyg.istiyorum.","On_isl.uyg.istemiyorum",v1,2,b)
c = ["Gauss_Bulanik","Keskinleştirme","Kenar_Bulma","Ortalama_Filtresi","Ortanca_Filtresi","Kontra_Hormanik Filtresi"]
yapim3 = my_struct(frame3,"Filtreleme uyg. istiyorum.","Filtreme uyg. istemiyorum.",v2,3,c)
d = ["B&W_Genişletme","B&W_Erozyon","İskelet_Çikarma"]
yapim4 = my_struct(frame3,"Morf.isl.uyg.istiyorum.","Morf.isl.uyg.istemiyorum.",v3,4,d)
lbl.pack(expand = "True")
window.mainloop()