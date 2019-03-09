from models import model
import re
import requests


class WordCounter():
    def count(url, keyword):
        r = requests.get(url)
        html_str = str(r.content, encoding='utf-8')
        result = re.findall('(^|\s)(' + keyword + ')($|\s)', html_str)
        return len(result)
