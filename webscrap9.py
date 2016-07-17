from urllib.request import urlopen

url = str(input())
textPage = urlopen(url)
print(str(textPage.read(), 'utf-8')
