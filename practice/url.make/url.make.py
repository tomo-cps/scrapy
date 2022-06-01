from urllib.request import urlopen
import urllib.request
import urllib.parse
import urllib

#for strpage in range(1,6):
#    html = urllib.request.urlopen('https://cookpad.com/search/%E3%83%91%E3%83%B3%E3%82%B1%E3%83%BC%E3%82%AD?page={0}'.format(strpage)).read() # html 取得
#    strhtml = str(html.decode('utf-8','replace'))
#    print(strhtml)

for strpage in range(10,50,10):
    html = urllib.request.urlopen('https://www.yelp.com/biz/marufuku-ramen-san-francisco-5?start={0}'.format(strpage)).read() # html 取得
    print(html)
#    strhtml = str(html.decode('utf-8','replace'))
#    print(strhtml)
