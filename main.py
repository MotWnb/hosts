import re
import requests
import os

url = 'https://github.com/malaohu/GitHubHosts'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.115 Safari/537.36 '
}
requests.packages.urllib3.disable_warnings()
proxies = {
    'http': 'http://223.82.60.202:8060'

}
request = requests.get(url, headers=headers, verify=False, timeout=1000000, proxies=proxies)
request.close()
request = request.text
# print(request)
request = re.compile(r'<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" '
                     r'data-snippet-clipboard-copy-content=".*?####################Github Start####################('
                     r'?P<name>.*?)# Last Update Time', re.S).finditer(request)
for i in request:
    message = i.group('name')
    print(message)
try:
    a = open(r'C:\Windows\System32\drivers\etc\hosts', 'a+')
    a.write('\n' + message)
    a.close()
    print(os.popen('ipconfig /flushdns').read())
finally:
    pass
