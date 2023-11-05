import urllib.request

urllib.request.urlretrieve("https://www.example.org/","webpage.html")

for line in open('webpage.html'):
    print(line.strip())