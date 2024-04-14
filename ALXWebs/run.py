from urllib.parse import urlsplit

url = "https://intranet.alxswe.com/projects/294"

split_url = urlsplit(url)

#print(dir(split_url))

print(split_url.count)
print(split_url.encode)
print(split_url.fragment)
print(split_url.geturl)
print(split_url.hostname)
print(split_url.index)
print(split_url.netloc)
print(split_url.password)
print(split_url.path)
print(split_url.port)
print(split_url.query)
print(split_url.scheme)
print(split_url.username)