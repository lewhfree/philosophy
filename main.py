import requests

from bs4 import BeautifulSoup

def getLink(title):
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/{title}"
    headers = {"User-Agent": "philosophyFinder/0.0.1 (github.com/lewhfree/philosophy)"}
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")

    for p in soup.find_all("p", recursive=True):
        for a in p.find_all("a", recursive=True):
            ref = a.get("href")
            if ref:
                return a['href'].split("/")[1]
    return None

target = "Philosophy"

start = "Bogosort"

current = start
print(current)

while target != current:
    current = getLink(current)
    print(current)
