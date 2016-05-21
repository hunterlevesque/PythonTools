# -*- coding:utf-8 -*-

import re
import urllib

def getHtml(url):
	m = urllib.urlopen(url)
	html = m.read()
	return html

def getData(html):
	pattern = r'<span class="title">(.+)</span>'
	p = re.compile(pattern)
	data = re.findall(p,html)
	return data

def main():
    my_file = 'my_file.txt'
    f = open(my_file,'wb')
    for x in range(0, 10):
        y = x * 25
        html = getHtml('https://movie.douban.com/top250?start=%d&filter=' %(25 * x))
        datas = getData(html)
        for stringex in datas:
            if stringex.find("&nbsp") == -1:
                y += 1
                f.write('第%d名'%y + stringex + '\n')

if __name__ == '__main__':
    main()

    #山丘