import datetime
import unittest

import jsondatetime as json
from dateutil.tz import tzutc
from parameterized import param, parameterized


class TestBase(unittest.TestCase):
    def setUp(self):
        self.test = '{"name": "John Doe", "born": "Thu, 1 Mar 2012 10:00:49 UTC"}'
        self.expected = datetime.datetime(2012, 3, 1, 10, 0, 49)

    def test_no_dates(self):
        test = '{"name": "John Doe"}'
        try:
            json.loads(test)
        except Exception as e:
            self.fail("Unexpected failure: %s" % e)

    @parameterized.expand(
        [
            param('{"key": "value"}', {"key": "value"}),
            param(
                '{"born": "2012-03-01T10:00:49+00:00", "name": "John Doe"}',
                {
                    "born": datetime.datetime(2012, 3, 1, 10, 0, 49, tzinfo=tzutc()),
                    "name": "John Doe",
                },
            ),
            param(
                '{"parent": {"date": "2020-02-20T02:20:02+00:00"}}',
                {
                    "parent": {
                        "date": datetime.datetime(2020, 2, 20, 2, 20, 2, tzinfo=tzutc())
                    }
                },
            ),
        ]
    )
    def test_equivalence(self, json_str, python):
        try:
            decoded = json.loads(json_str)
        except Exception as e:
            self.fail("Unexpected failire: %s" % e)
        self.assertEqual(decoded, python)
        back_again = json.dumps(python, sort_keys=True)
        self.assertEqual(back_again, json_str)

    def test_object_hook(self):
        def hook(dct):
            dct["hookjob"] = "I'm hooked!"
            return dct

        decoded = json.loads(
            '{"name": "John Doe", "born": "Thu, 1 Mar 2012 10:00:49 UTC"}',
            object_hook=hook,
        )
        self.assertEqual(
            decoded.get("born"),
            datetime.datetime(2012, 3, 1, 10, 0, 49, tzinfo=tzutc()),
        )
        self.assertIn("hookjob", decoded)


if __name__ == "__main__":
    unittest.main()
