from models import model
import re
import requests


class WordCounter():
    def count_from_url(self, url, keyword):
        r = requests.get(url)
        html_str = str(r.content, encoding='utf-8')
        last_modified = r.headers.get('Last-Modified]')
        result = self.count_from_string(html_str, keyword)
        self.save_record_to_db(url, keyword, result, last_modified)
        return {"count": result}

    def count_from_string(self, string, keyword):
        result = re.findall("\\b(" + keyword + ")\\b", string)
        return len(result)
    
    def save_record_to_db(self, url, keyword, result, last_modified):
        record = model.Record(url, keyword, result, last_modified)
        record.add()
        