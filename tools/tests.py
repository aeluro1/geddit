import unittest
import requests

import geddit

class Tests(unittest.Test):
    
    def test_image_download_success(self):
        url = "https://i.imgur.com/"
        response = requests.get(url)

    def test_imgur_gallery_urls(self):
        pass



if __name__ == "__main__":
    unittest.main()