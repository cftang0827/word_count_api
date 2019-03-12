import unittest
import app

from models import model


class TestAppIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.test_word = "Bazel"
        self.test_url = "https://docs.bazel.build/versions/master/install-ubuntu.html#install-with-installer-ubuntu"

    def tearDown(self):
        self.app = None
        self.test_word = None
        self.test_url = None

    def test_ok_case(self):
        resp = self.app.post(
            '/wordcount', json={
                "word": self.test_word,
                "url": self.test_url
            })

        self.assertEqual(resp.status_code, 200, 'No 200, error')

    def test_html_last_modified_cache(self):
        resp = self.app.post(
            '/wordcount', json={
                "word": self.test_word,
                "url": self.test_url
            })

        get_from_db = model.session.query(model.Record).filter_by(
            word=self.test_word, url=self.test_url).all()

        self.assertEqual(
            len(get_from_db), 1,
            "Last Modified Cache not work duplcate data ..")

    def test_wrong_method_405(self):
        resp = self.app.get('/wordcount')

        self.assertEqual(
            resp.status_code, 405,
            'It should be 405 status code, but not the correct one')

    def test_not_found_404(self):
        resp = self.app.post('wordcount2')
        self.assertEqual(
            resp.status_code, 404,
            'It should be 404 status code, but not the correct one')

    def test_internal_server_error_500(self):
        resp = self.app.post(
            '/wordcount', json={
                "word": self.test_word,
                "url": "abc",
            })
        self.assertEqual(
            resp.status_code, 500,
            'It should be 500 status code, but not the correct one')
