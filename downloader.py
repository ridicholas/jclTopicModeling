import requests
from bs4 import BeautifulSoup

def download(link):
    response = requests.get(link)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    body = parser.body
    p=body.p
    print(content)
    head = parser.head
    title = head.title
    title_text = title.text
