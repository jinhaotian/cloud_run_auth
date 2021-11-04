import unittest
from mcs import MediaCollectionService;

class TestStringMethods(unittest.TestCase):

    def test_get(self):
        mcs = MediaCollectionService("https://mcs-load-4sdci277xa-uw.a.run.app")
        resp = mcs.get_favorites("8C54EEA3387AD457E050960A5503661F","videos")
        print(resp["items"])
        self.assertTrue(len(resp["items"]) >= 1)
    

    def test_favorite(self):
        mcs = MediaCollectionService("https://mcs-load-4sdci277xa-uw.a.run.app")
        get_resp = mcs.get_favorites("8C54EEA3387AD457E050960A5503661F","videos")
        add_resp = mcs.add_favorites("8C54EEA3387AD457E050960A5503661F","videos","vid.123")
        get_resp_n = mcs.get_favorites("8C54EEA3387AD457E050960A5503661F","videos")
        delete_resp = mcs.remove_favorites("8C54EEA3387AD457E050960A5503661F","videos","vid.123")
        self.assertTrue(add_resp == 201)
        self.assertTrue(delete_resp == 200)
        self.assertTrue(len(get_resp_n["items"]) - len(get_resp["items"])  ==  1)
        print(add_resp)
    
    def test_contain(self):
        mcs = MediaCollectionService("https://mcs-load-4sdci277xa-uw.a.run.app")
        add_resp = mcs.add_favorites("8C54EEA3387AD457E050960A5503661F","videos","vid.123")
        contain_resp = mcs.contains("8C54EEA3387AD457E050960A5503661F","videos","vid.123")
        delete_resp = mcs.remove_favorites("8C54EEA3387AD457E050960A5503661F","videos","vid.123")
        self.assertTrue(add_resp == 201)
        self.assertTrue(delete_resp == 200)
        self.assertTrue(contain_resp[0])
        print(contain_resp)
    
    def test_count(self):
        mcs = MediaCollectionService("https://mcs-load-4sdci277xa-uw.a.run.app")
        count_resp = mcs.count("8C54EEA3387AD457E050960A5503661F","videos")
        self.assertTrue(count_resp["total"] == 1)
        print(count_resp)
if __name__ == '__main__':
    unittest.main()