# import unittest-xml-reporting
import xmlrunner
import unittest
import requests

urlbase = 'http://localhost:8888/v1'

class TestRESTApp(unittest.TestCase):

    def test_v1(self):
        r = requests.get(urlbase)
        self.assertEqual(r.text,'OpenSource Software API v1')
        self.assertEqual(r.status_code, 200,'API Return Code Failed')

    def test_list(self):
        r = requests.get(urlbase+"/list")
        self.assertEqual(r.status_code, 200,'API Return Code Failed')

    def test_add(self):
        name = 'SampleOSPackage'
        short_description = 'The sample description'
        site = 'http://www.sampleospackage.wi.us'
        r = requests.get(urlbase+"/add_OpenSourceSoftware", 
                data = {
                    'name':name,
                    'short_description': short_description,
                    'site': site
                }
            )
        self.assertEqual(r.status_code, 200,'API Return Code Failed')

    def test_delete(self):
            name = 'SampleOSPackage'
            r = requests.get(urlbase+"/delete_OpenSourceSoftware", 
                    data = {
                        'name':name
                    }
                )
            self.assertEqual(r.status_code, 200,'API Return Code Failed')

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure thta some options that are not applicable
        # remain hidden from the help menu
        failfast=False, buffer=False, catchbreak=False
    )