from urllib.request import urlopen

url = str(input())
textPage = urlopen(url)
print(textPage.read())
