import json
import datetime
import dateutil.parser

DEFAULT_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S UTC'
DEFAULT_ARGUMENT = "datetime_format"

class DatetimeJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(obj)

json._default_encoder = DatetimeJSONEncoder


def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
          allow_nan=True, cls=None, indent=None, separators=None,
          encoding='utf-8', default=None, sort_keys=False, **kw):
    return json.dumps(obj, skipkeys=skipkeys, ensure_ascii=ensure_ascii,
                      check_circular=check_circular, allow_nan=allow_nan,
                      cls=cls, indent=indent, separators=None, encoding=encoding,
                      default=default, sort_keys=sort_keys, **kw)

def loads(s, **kwargs):

    source = json.loads(s, **kwargs)

    return iteritems(source, format)

def iteritems(source, format):

    for k, v in source.items():
        if isinstance(v, list):
            for a in v:
                iteritems(a, format)
        elif isinstance(v, dict):
            iteritems(v, format)
        elif isinstance(v, basestring):
            try:
                source[k] = dateutil.parser.parse(v, ignoretz=True)
            except:
                pass

    return source