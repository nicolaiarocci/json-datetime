# jsondatetime

[![image](https://travis-ci.com/schibsted/json-datetime.svg?branch=master)](https://travis-ci.com/schibsted/json-datetime)

`jsondatetime` allows for proper decoding of datetime values contained in
JSON streams.

## The problem

The JSON standard RFC 4627 does not support datetime types. These are
usually represented as strings and Python decoders end up decoding them
as such. Consider the following example:

``` python
import simplejson as json

>>> test = '{"name": "John Doe", "born": "Thu, 1 Mar 2012 10:00:49 UTC"}'
>>> json.loads(test)
{'born': u'Thu, 1 Mar 2012 10:00:49 UTC', 'name': u'John Doe'}
```

As you can see, in the resulting dictionary `born` is still a string.

## The solution

`jsondatetime` is a very simple wrapper around Python simplejson `loads`
and `dumps` methods. It decodes datetime values contained in JSON
strings:

``` python
import jsondatetime as json

>>> test = '{"name": "John Doe", "born": "Thu, 1 Mar 2012 10:00:49 UTC"}'
>>> j = json.loads(test); j
{'name': 'John Doe', 'born': datetime.datetime(2012, 3, 1, 10, 0 ,49, tzinfo=tzutc())}
>>> dumps(j)
"{'name': 'John Doe', 'born': '2012-03-01T10:00:49+00:00'}"
```

Strings are parsed using `dateutil.parser.parse` which is fairly
flexible for common datetime formats.

## Custom parsing

Being just a wrapper around the `loads` method, you can still use all
the standard `loads` arguments, `object_hook` included. This means that
you can still perform custom parsing of your inbound JSON stream.

## Installation

`pip install jsondatetime`
