import datetime
import functools
import json

import dateutil.parser

try:
    string_types = basestring  # Python 2
except NameError:
    string_types = str  # Python 3


class DatetimeJSONEncoder(json.JSONEncoder):
    def __init__(self, **kwargs):
        super(DatetimeJSONEncoder, self).__init__(**kwargs)
        if kwargs.get("default") is not None:
            self.default = kwargs.get("default")

    def default(self, o):  # (pylint bug 414) pylint: disable=method-hidden
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return super(DatetimeJSONEncoder, self).default(o)


dumps = functools.partial(json.dumps, cls=DatetimeJSONEncoder)


def loads(s, **kwargs):
    source = json.loads(s, **kwargs)
    return iteritems(source)


def iteritems(source):
    for k, v in source.items():
        if isinstance(v, list):
            for a in v:
                iteritems(a)
        elif isinstance(v, dict):
            iteritems(v)
        elif isinstance(v, string_types):
            try:
                source[k] = dateutil.parser.parse(v)
            except (ValueError, OverflowError):
                pass

    return source
