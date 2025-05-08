import requests

from bs4 import BeautifulSoup
import urllib
def getLink(title):
    title2 = urllib.parse.quote(title)
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/{title2}"
    headers = {"User-Agent": "philosophyFinder/0.0.1 (github.com/lewhfree/philosophy)"}
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")

    for p in soup.find_all("p", recursive=True):
        for a in p.find_all("a", recursive=True):
            ref = a.get("href")
            if ref and "#cite_note" not in ref and "Help:" not in ref and "" != ref:
                return a['href'].split("/")[1]
    return None
index = 0

worked = set()
failed = set()

while True:
    seen = set()

    target = "Philosophy"

    index += 1

    with open("titles.txt", "r") as file:
        for i, line in enumerate(file, start=1):
            if i == index:
                start = line.strip()
                break
           
    current = start
    print(current)
    seen.add(current)

    
    while target != current:
        current = getLink(current)
        print(current)
        if current in seen or current in failed:
            print("Seen before, loop")
            with open("failed.txt","a") as bile:
                bile.write(start + "\n")
            failed.add(start)
            failed.update(seen)
            break
        else:
            seen.add(current)
    else:
        print("Seen " + str(len(seen)))

        with open("worked.txt", "a") as dfile:
            dfile.write(start + "\n")
        worked.add(start)
        worked.update(seen)
