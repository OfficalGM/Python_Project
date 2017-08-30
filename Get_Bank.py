# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

class Foreign_Exchange_Rate:
    def __init__(self):
        url = 'http://rate.bot.com.tw/xrt?Lang=zh-TW'
        html = requests.get(url).text
        self.soup = BeautifulSoup(html, 'html.parser')
        self.__Get_All()
    def main(self):
        time = str(self.soup.select('.time')).split('>')[1].split('<')[0]
        print time
        print self.all
    def __Get_All(self):
        rows=self.soup.find('table',{'class','table table-striped table-bordered table-condensed table-hover'}).tbody.find_all('tr')
        temp=[]
        all=[]
        for row in rows:
               temp.append([s for s in row.stripped_strings])
        for i in temp:
            all.append([i[0],i[2],i[3],i[4],i[5]])
        self.all=all



