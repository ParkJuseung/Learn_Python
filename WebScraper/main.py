import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser") #데이터를 추출하는 역할

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')
spans = []
for page in pages:
    spans.append(page.find("span"))
print(spans[0:-1])
