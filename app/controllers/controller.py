import re

import requests

from models import model


class WordCounter():
    '''
    The word counter module, that can count number of keyword in url and save it to the DB
    '''

    def count_from_url(self, url, keyword):
        '''
        Args: 
            url (str): The url that you want to analyze
            keyword (str): The keyword that you want to find in url
        
        Returns:
            dict: The return value is the count of keyword in url
            {
                "count": number (int)
            }
        '''
        # get the page from url
        r = requests.get(url)
        html_str = str(r.content, encoding='utf-8')

        # check the http last modified time, if it was already existed in table
        # use cache rather than analyzing again
        last_modified = r.headers.get('Last-Modified')

        result, need_to_save_db = self.get_result(url, html_str, keyword,
                                                  last_modified)

        if need_to_save_db:
            self.save_record_to_db(url, keyword, result, last_modified)
        return {"count": result}

    def get_result(self, url, html_str, keyword, last_modified):
        '''
        To calculate the number of keyword in html_str, and before doing real analyzing,
        fetch the record by using last_modified to find whether the record had already done
        before, to save the computing power of server
        
        Args:
            url (str): The url that you want to analyze
            html_str (str): The html string that requested from url
            keyword (str): The keyword that you want to find in url
            last_modified (str): HTTP last_modified of website
        
        Returns:
            tuple: (The count number (int), need_to_save_db (boolean))

        '''
        record_query_cache = model.Record(url, keyword)
        record_query_cache.query()
        if last_modified is not None and record_query_cache.result is not None:
            if record_query_cache.last_modified == last_modified:
                return (record_query_cache.result, False)
        return (self.count_from_string(html_str, keyword), True)

    def count_from_string(self, string, keyword):
        '''
        Private method for count number of keyword in string
        '''
        string_no_tag = self.clean_html(string)
        result = re.findall("\\b(" + keyword + ")\\b", string_no_tag)
        return len(result)

    @staticmethod
    def clean_html(html_str):
        clean_regex = re.compile('<.*?>')
        cleantext = re.sub(clean_regex, '', html_str)
        return cleantext

    @staticmethod
    def save_record_to_db(url, keyword, result, last_modified):
        '''
        Save the record of analyzing to the Record DB
        '''
        record = model.Record(url, keyword, result, last_modified)
        record.add()
