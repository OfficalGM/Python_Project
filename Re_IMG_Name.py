# -*- coding: utf-8 -*-
import os
import sys
class ReFileName:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        positon = os.getcwd()
        self.positon =positon
        self.__ReName()

    def __ReName(self):
        list_dirs = os.walk(self.positon, topdown=True)
        for root, dirs, files in list_dirs:
            num = 0
            for name in files:
                filename=os.path.join(root,name)
                file_format=os.path.splitext(name)[1]
                if file_format=='.jpg' or file_format=='.png':
                   try:
                        os.rename(filename, filename.replace(name, str(num)+file_format))
                   except Exception as e:
                       print e
                num+=1






if __name__ == '__main__':
    A=ReFileName()
    raw_input("Press Enter to terminate.")

