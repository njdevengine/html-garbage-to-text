import urllib
from bs4 import BeautifulSoup

url = "https://www.reddit.com"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
new_text = []
for i in text.split(" "):
    if len(i)<20:
        new_text.append(i)
        print(i, end=" ")
(" ").join(new_text)
