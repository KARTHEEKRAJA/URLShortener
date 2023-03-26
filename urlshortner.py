import pyshorteners
url = input("Enter the url: ")
shorteners = pyshorteners.Shortener()
k = shorteners.tinyurl.short(url)
print(k)