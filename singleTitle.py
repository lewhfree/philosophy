import requests

from bs4 import BeautifulSoup

def getRandomTitle():
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "1"
    }

    request = requests.get(url=url, params=params)
    data = request.json()

    random = data["query"]["random"]
    for r in random:
       return r["title"] 

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

seen = set()

target = "Philosophy"

index = 1

with open("titles.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        if i == index:
            start = line.strip()

print(start)

current = start
print(current)
seen.add(current)

while target != current:
    current = getLink(current)
    print(current)
    if current in seen:
        print("Seen before, loop")
        with open("failed.txt","a") as file:
            file.write(start + "\n")
        exit()
    else:
        seen.add(current)

print("Seen " + str(len(seen)))

with open("worked.txt", "a"):
    file.write(start + "\n")
