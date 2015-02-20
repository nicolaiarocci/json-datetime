from unittest import TestCase

import jsondatetime as json
import datetime

class TestBase(TestCase):

    def setUp(self):
        self.test = '{"name": "John Doe", "born": "Thu, 1 Mar 2012 10:00:49 UTC"}'
        self.expected = datetime.datetime(2012, 3, 1, 10, 0 ,49)
        self.datetime_format = '%a, %d %b %Y %H:%M:%S UTC'

    def test_no_dates(self):
        test = '{"name": "John Doe"}'
        try:
            json.loads(test)
        except Exception as e:
            self.fail("Unexpected failure: %s" % e)

    def test_default_date_format(self):
        decoded = json.loads(self.test).get('born')
        self.assertIs(type(decoded), datetime.datetime)
        self.assertEqual(decoded, self.expected)

    def test_date_format(self):
        test = '{"born": "Thu, 1 Mar 2012"}'
        expected = datetime.datetime(2012, 3, 1)
        decoded = json.loads(test).get('born')
        self.assertIs(type(decoded), datetime.datetime)
        self.assertEqual(decoded, expected)

    def test_object_hook(self):
        decoded = json.loads(self.test, object_hook=self.hook)
        self.assertEqual(decoded.get('born'), self.expected)
        self.assertIn("hookjob", decoded)

    def test_nested_dicts(self):
        test = '{"updated": {"$gte": "Thu, 1 Mar 2012 10:00:49 UTC"}}'
        decoded = json.loads(test).get('updated').get('$gte')
        self.assertIs(type(decoded), datetime.datetime)
        self.assertEqual(decoded, self.expected)

    def hook(self, dct):
        dct["hookjob"] = "I'm hooked!"
        return dct

