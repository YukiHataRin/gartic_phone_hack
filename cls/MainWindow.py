import tkinter
import os
from PIL import Image, ImageTk, ImageFilter
from cls.Get_Pic import Get_Pic
from tkinter import messagebox
from cls.AutoDrawing import Auto_Drawing

class MainWindow():
    def __init__(self):
        self.font = "新細明體, 12"
        self.win = tkinter.Tk()
        self.win.geometry("800x450+300+200")
        self.win.title("自動繪畫")
        self.__widget()
        self.pic = []
        self.get_pic = Get_Pic()
        self.index = 0
        self.auto_draw = Auto_Drawing()
        
    def __widget(self):
        self.doublevar = tkinter.DoubleVar(self.win)
        self.button_next = tkinter.Button(self.win, font = self.font, text = "下一張", command = self.__next)
        self.button_prev = tkinter.Button(self.win, font = self.font, text = "上一張", command = self.__prev)
        self.button_ok = tkinter.Button(self.win, font = self.font, text = "開始繪圖", command = self.__run)
        self.button_search = tkinter.Button(self.win, font = self.font, text = "搜尋", command = self.__search)
        self.entry_search = tkinter.Entry(self.win, font = self.font)
        self.entry_search.bind("<Return>", lambda x: self.__search())
        self.entry_multi = tkinter.Entry(self.win,textvariable = self.doublevar, width = 10)
        self.label_text = tkinter.Label(self.win, text = "縮放倍率", font = self.font)
        self.label_img = tkinter.Label(self.win)
        self.doublevar.set(1.0)

    def __search(self):
        try:
            if self.entry_search.get() == "":
                raise EOFError
            
            self.pic = self.get_pic.get_pic(self.entry_search.get())
            messagebox.showinfo("成功", f"搜尋 {self.entry_search.get()} 成功")
            self.index = 0
            self.__showpic()

        except:
            messagebox.showerror("錯誤", "發生錯誤!")

    def __showpic(self):
        try:
            if self.index >= len(self.pic):
                self.index = 0
            
            imgtk = ImageTk.PhotoImage(self.pic[self.index])
            self.label_img.configure(image = imgtk)
            self.label_img.image = imgtk
        
        except:
            messagebox.showerror("錯誤", "沒有圖片!")

    def __prev(self):
        self.index -= 1
        self.__showpic()

    def __next(self):
        self.index += 1
        self.__showpic()

    def __run(self):
        pic = self.pic[self.index]
        self.win.state("icon")
        self.auto_draw.run(pic.resize((int(pic.size[0] * self.doublevar.get()), int(pic.size[1] * self.doublevar.get()))))
        self.win.wm_attributes("-topmost", -1)

    def start_app(self):
        self.entry_search.place(x = 20, y = 10)
        self.button_search.place(x = 140, y = 50)
        self.label_img.place(x = 300, y = 100)
        self.button_prev.place(x = 20, y = 150)
        self.button_next.place(x = 110, y = 150)
        self.label_text.place(x = 20, y = 220)
        self.entry_multi.place(x = 20, y = 250)
        self.button_ok.place(x = 80, y = 280)

        self.win.mainloop()

if __name__ == "__main__":
    MainWindow().show()