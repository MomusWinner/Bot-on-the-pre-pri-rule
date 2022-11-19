import requests
import bs4


def SearchWordDefinition(word,numberOfLetters) -> str:
    response = requests.get('https://kartaslov.ru/значение-слова/' + word)
    page = bs4.BeautifulSoup(response.content,"html.parser")
    PageItem = page.find('li', "v2-dict-entry-text")
    return PageItem.text[:numberOfLetters] + " ..."
