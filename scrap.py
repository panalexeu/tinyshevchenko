# minimal script that scraps poems from ukrlib 
import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm

from urllib.parse import urljoin


_author_url = 'https://www.ukrlib.com.ua/books/author.php?id=1'
_pages = 14

def _preproc(text: str):
    lines = [line.strip() for line in text.splitlines()]
    return '\n'.join(line for line in lines if line)

if __name__ == '__main__':
    hrefs = [] 
    for page in tqdm(range(_pages), desc='pages'): 
        if page == 0: 
            url = _author_url
        else: 
            url = _author_url + '&page=' + str(page+1)

        page_content = requests.get(url).text
        soup = BeautifulSoup(page_content, 'html.parser')
        hrefs += [urljoin(url, a['href']) for a in soup.select('div.content ul.list a')]
    assert len(hrefs) == 20 * 13 + 1 # sanity check, the amount of hrefs on ukrlib should be 261

    # not poems/plays 
    ignore_hrefs = [
        'printit.php?tid=15371', # Автобіографічний нарис
        'printit.php?tid=719',   # Близнецы
        'printit.php?tid=748',   # Листи до А. Лизогуба 
        'printit.php?tid=790',   # Художник
        'printit.php?tid=15370', # Щоденник 
    ]
    hrefs = [h for h in hrefs if not h.endswith(tuple(ignore_hrefs))]
    assert len(hrefs) == 20*13+1 - len(ignore_hrefs)

    poems = []
    for href in tqdm(hrefs, desc='poems'): 
        page_content = requests.get(href).text
        soup = BeautifulSoup(page_content, 'html.parser')
        article = soup.find('article')
        for tag in article.select('div.readalser'):
            tag.decompose()
        text = article.text 
        proc_text = _preproc(text)
        poems.append(proc_text)

    with open('./tinyshevchenko.txt', 'w') as f: 
        f.write('\n'.join(poems))