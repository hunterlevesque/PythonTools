# -*- coding:utf-8 -*-

import os
import time
import random

############需要配置的地方########################
#网页的title
HEAD_TITLE = "XX项目测试包"

# ip地址：格式：127.0.0.1
IP = "127.168.XX.81"

# 放置包的位置 例如：/usr/local/var/www/
FILE_DIR = "/usr/local/var/www/"

# 跑马灯展示当前的任务
CURRENT_WORK_LIST = "当前的测试任务：魔窗功能"

#每个包修改的东西叙述
def getArray():
	return [	
		"代码合并，修复登录失败的bug",
		]
###############################################

def getFileModifyTime(fileName):
	filePath = "%s%s"%(FILE_DIR, fileName)
	print(filePath)
	a = time.localtime(os.stat(filePath).st_mtime)
	return time.strftime("%m-%d %H:%M",a)

# log: 之前根据文件名排名，现在根据文件的创建时间去倒序排名
def compare(x, y):  
	stat_x = os.stat(FILE_DIR + x)
	stat_y = os.stat(FILE_DIR + y)
	if stat_x.st_ctime > stat_y.st_ctime:
		return -1
	elif stat_x.st_ctime < stat_y.st_ctime:
		return 1
	else:
		return 0 

def getFilelist():
	fileName = []
	for file in os.listdir(FILE_DIR):
		if file.find(".apk") != -1 or file.find(".ipa") != -1:
			fileName.insert(0, file)
	# 给列表排名
	fileName.sort(compare)	
	return fileName

def getHtmlTxt():
	return '''
<!DOCTYPE html>
<html>
<head>
	<title>%s</title>

	<meta charset="UTF-8">
	<style type="text/css">
		body {
			background-color: #F5F5DC;
		}

		label {
			color: #7A378B;
		}

		  #name {
		  	position:fixed;
		  	bottom: 0px;
		  	right:0px;
		  }

		 #gif {
		 	position:fixed;
		  	top: 10px;
		  	right:0px;
		 }
	  #fontSet {color: #008B8B;}
	</style>

</head>
<body>
	<h1 id="title"> %s </h1>
	<marquee width=1000 behavior=scroll direction=left align=middle><FONT color=#6FB7B7>%s</marquee>

	<ul id="list">
		<script type="text/javascript">		
			%s
		</script>
	</ul>

	<br/>
	<br/>
	<br/>
	<br/>
	<br/>
	<p><em>Thank you for test.</em></p>
</body>
</html>
'''

def writeFile(fileNameArray):
	print(fileNameArray)
	infoArray = getArray()
	file_object = open("index.html","w")
	try:
		write_text = getHtmlTxt()
		string = ""
		for x in xrange(0,len(fileNameArray)):
			print(x)
			string = string + '''document.write('<li><a href="http://%s/%s">%s</a><label>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp %s</label></li><p id="fontSet">%s<p></br></br><hr />')\n'''%(IP, fileNameArray[x], fileNameArray[x], getFileModifyTime(fileNameArray[x]), infoArray[x])
			
		write_text = write_text%(HEAD_TITLE, HEAD_TITLE, CURRENT_WORK_LIST, string)
		file_object.writelines(write_text)
		file_object.close()

	except Exception as e:
		file_object.close()

def main():
	writeFile(getFilelist())	

if __name__ == '__main__':
	main()

# <img id="gif" alt="" src="%s"/>
# <video autoplay="autoplay" id="name" loop="loop"> 
# 	<source src="%s" type="video/mp4">
# </video>
