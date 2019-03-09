from models import model
import re
import requests


class WordCounter():
    def count_from_url(self, url, keyword):
        r = requests.get(url)
        html_str = str(r.content, encoding='utf-8')
        return self.count_from_string(html_str, keyword)

    def count_from_string(self, string, keyword):
        result = re.findall('(^|\s)(' + keyword + ')($|\s)', string)
        return len(result)
