import urllib, urllib2, sys
from bs4 import BeautifulSoup, Comment
reload(sys)
sys.setdefaultencoding('utf-8')
dirs="./"
level=1
fname=dirs+"chap"+str(level)+".txt"
level=level+1
outputFile=open(fname,'a')
url1='https://thirukkural133.wordpress.com/2011/11/12/chapter-1-invocation-2/'
content1 = urllib2.urlopen(url1).read()
soup1 = BeautifulSoup(content1, "html.parser")

#extracts meanings in l1
l1=[]
for row in soup1('table')[0].tbody('tr'):
    tds = row('td')
    l1.append(tds[0].text)

#extracts actual tirukkural
l2=[]
for row in soup1('table')[1].tbody('tr'):
    tds = row('td')
    l2.append(tds[0].text)

#write the heading
heading='\t\t'+str(l1[1])
outputFile.write(heading)

l1=l1[2:] #data is unstructured changed for structuring

for i,j in zip(l1,l2):
	h=j+'\n'+i+'\n'
	outputFile.write(h)
link=soup1('div',attrs={"class" : "nav-next"})

for lin in link[1]('a'):
	url1=lin.get('href')

print "next url is\n"+url1

#make it recursive for all url , make func def:
