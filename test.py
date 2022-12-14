import urllib.request, re, ssl
s = urllib.request.urlopen("https://172.17.8.127:8080/login?username=Admin&password=12345", context=ssl._create_unverified_context()).read()
for x in s.replace("\n", "").split("{"):
    m = re.search('"name"\s*\:\s*"(.*?)".*Channel', x)
    if not m: continue
    print (m.group(1))
    