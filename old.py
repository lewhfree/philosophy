import wikipediaapi as wikipedia
import time
userAgentString = "PhilosophyChecker/0.0.1 (github.com/lewhfree/philosophy)"

wiki = wikipedia.Wikipedia(user_agent=userAgentString, language='en', extract_format=wikipedia.ExtractFormat.HTML)

def firstKey(keys, text):
    positions = {
        key: text.find(key) for key in keys if key in text
    }

    if not positions:
        return None
    return min(positions, key=positions.get)

startArticle = "Bogosort"

currArticle = startArticle

reached = set()

target = "Philosophy"

while target !=  currArticle:
    reached.add(currArticle)
    
    page = wiki.page(currArticle)
    print(page.text)
    links = page.links

    first = next(iter(links.items()))
    print(first)

    print(firstKey(links.keys(), page.text))

    time.sleep(100)

    if not page.exists():
        print("Article doesn't exist")
