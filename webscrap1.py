from urllib.request import urlopen
html = urlopen("http://www.georgeharrison.com/")
print(html.read())
