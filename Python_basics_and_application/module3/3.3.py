import requests
import re


# url_a = 'https://stepik.org/media/attachments/lesson/24472/sample0.html'.replace('stepik.org', 'stepic.org')
# url_b = 'https://stepik.org/media/attachments/lesson/24472/sample2.html'.replace('stepik.org', 'stepic.org')

url_a = input().replace('stepik.org', 'stepic.org')
url_b = input().replace('stepik.org', 'stepic.org')

a = requests.get(url_a)
a_cont = a.text


pattern = r"""(?:https?:\/\/|ftps?:\/\/|www\.)(?:(?![.,?!;:()]*(?:\s|$|"))[^\s"]){2,}"""
a_urls = re.findall(pattern=pattern, string=a_cont)

ans = None
all_links = list()
for url in a_urls:
    content = re.findall(pattern=pattern, string=requests.get(url).text)
    if url_b in content:
        ans = True
if ans:
    print('Yes')
else:
    print('No')
