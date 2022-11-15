import unittest
import requests as req

class TestAPI(unittest.TestCase):
    url="http://127.0.0.1:5000/metrics"

    def test_case_1(self):
        try:
            resp=req.get(self.url)
            self.assertEqual(resp.status_code, 2000)
            print("Test 1 Passed:)")
        except:
            print("Test case 1 Failed :(")

if __name__=="__main__":
    test = TestAPI()
    print("Testing Started ")
    test.test_case_1()