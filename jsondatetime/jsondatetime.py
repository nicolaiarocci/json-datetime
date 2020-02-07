import datetime
import functools
import json

import dateutil.parser

try:
    string_types = basestring  # Python 2
except NameError:
    string_types = str  # Python 3


class DatetimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        super(DatetimeJSONEncoder, self).default(obj)


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
            except:
                pass

    return source
