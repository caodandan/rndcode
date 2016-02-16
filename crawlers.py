import urllib
import re

def getHtml(url):
	page=urllib.urlopen(url)
	html = page.read()
	return html
	
def getImage(html):
	reg = r'imgsrc"(.*?\.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x=1
	for i in imglist:
		urllib.urlretrieve(i,'%s.jpg'%x)
		x+=1
	
html = getHtml("http://image.baidu.com/search/index?ct=201326592&st=-1&cl=2&lm=-1&nc=1&rps=2&ie=utf-8&tn=baiduimage&pv=&fm=rs2&word=%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87%E7%BE%8E%E5%A5%B3&ofr=%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87")
#html.getHtml() 
print getImage(html)