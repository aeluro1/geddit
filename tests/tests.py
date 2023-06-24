import unittest
import requests

import geddit

class Tests(unittest.TestCase):

    def test_image_download_success(self):
        url = "https://i.imgur.com/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_imgur_gallery_urls(self):
        pass


if __name__ == "__main__":
    unittest.main()