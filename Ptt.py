# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import sys

class Ptt_crawler:
    def __init__(self,data):
        reload(sys)
        sys.setdefaultencoding('utf8')
        url='https://www.ptt.cc/bbs/Beauty/index.html'
        html = requests.get(url).text
        self.soup = BeautifulSoup(html, 'html.parser')
        index=self.soup.find_all('a',{'class','btn wide'})
        page=[]
        for i in index:
            page.append(str(i['href']).split('.html')[0].split('index')[1])
        del page[page.index(''):]
        page=[data,page[1]]
        print page
        self.page=page
        self.__crawler_link_and_title()
    def __crawler_link_and_title(self):
        for p in xrange(int(self.page[0]),int(self.page[1])+1):
            url='https://www.ptt.cc/bbs/Beauty/index'+str(p)+'.html'
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            row=soup.find_all('div',{'class','r-list-container action-bar-margin bbs-screen'})
            for i in row:
                col=i.find_all('a')
                for j in col:
                    Not_in=str(j['href']).split('/bbs/Beauty/')[1]
                    if Not_in!='M.1503988534.A.5A2.htm' and Not_in !='M.1476111251.A.C20.html' and Not_in !='M.1430099938.A.3B7.html' \
                        and Not_in !='M.1423752558.A.849.html' and Not_in!='M.1443906121.A.65B.html' and Not_in!='M.1503988534.A.5A2.html':
                        link='https://www.ptt.cc'+j['href']
                        title=j.text.strip()
                        self.__crawler_content(link,title)
    def __crawler_content(self,link,title):
        positon = os.getcwd()
        url=link
        fname=unicode(positon+'\\'+title)
        try:
            html = requests.get(url).text
            soup=BeautifulSoup(html, 'html.parser')
            row=soup.select('div .richcontent a')
            num = 0
            for i in row:
                if not os.path.isdir(fname):
                    os.makedirs(fname)
                jpg_link='http:'+str(i['href'])+'.jpg'
                pic = requests.get(jpg_link)
                fp=open(fname+'\\'+unicode(title)+str(num)+'.jpg','wb')
                fp.write(pic.content)
                fp.close()
                num += 1
        except Exception as msg:
            print msg
if __name__ == '__main__':
    ptt=Ptt_crawler(2260)
