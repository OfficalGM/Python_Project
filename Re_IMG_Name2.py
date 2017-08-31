# -*- coding: utf-8 -*-
from Tkinter import *
import os
import sys
import time
class MyApplication():
    def __init__(self,master):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.master=master
        self.master.title('ReName')
        self.label1=Label(self.master,text="檔案路徑:").grid(row=0)
        self.label2=Label(self.master,text="重新命名:").grid(row=1)
        self.Entry1=Entry(self.master)
        self.Entry1.grid(row=0,column=1)
        self.Entry2=Entry(self.master)
        self.Entry2.grid(row=1,column=1)
        self.button=Button(self.master,text="確認",command=self.Print_button).grid(row=2,column=4)
        self.master.mainloop()
    def Print_button(self):
        if len(self.Entry1.get())>0:
            position=self.Entry1.get()
            DataName=str(self.Entry2.get())
            Re=ReFileName(position,DataName)
            if int(Re.value)==1:
                self.master.destroy()
class ReFileName:
    def __init__(self,position,DataName):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.positon =position
        self.__ReName(DataName)

    def __ReName(self,DataName):
        list_dirs = os.walk(self.positon, topdown=True)
        for root, dirs, files in list_dirs:
            num = 0
            for name in files:
                filename=os.path.join(root,name)
                file_format=os.path.splitext(name)[1]
                print filename
                if file_format=='.jpg' or file_format=='.png':
                   try:
                        os.rename(filename, filename.replace(name, DataName+'_'+str(num)+file_format))
                   except Exception as e:
                       print e
                num+=1
        self.value=1
if __name__ == '__main__':
    master = Tk()
    T=MyApplication(master)

