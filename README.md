# JSON-datetime
JSON-datetime allows for proper decoding of datetime values contained in JSON
streams.

[![Build Status](https://secure.travis-ci.org/nicolaiarocci/json-datetime.png?branch=master)](http://travis-ci.org/[YOUR_GITHUB_USERNAME]/[YOUR_PROJECT_NAME])

## The problem
The JSON standard ([RFC 4627](http://www.ietf.org/rfc/rfc4627.txt)) does not
support datetime types. These are usually represented as strings and Python 
decoders end up decoding them as such. Consider the following example:
```python
    import simplejson as json

    >>> test = '{"name": "John Doe", "born": "Thu, 1 Mar 2012 10:00:49 UTC"}'
    >>> json.loads(test)
    {'name': 'John Doe', 'born': 'Thu, 1 Mar 2012 10:00:49 UTC'} 
```
As you can see, in the resulting dictionary `born` is still a string.

## The solution
JSON-datetime is a very simple wrapper around Python
[simplejson](http://simplejson.readthedocs.org/en/latest/index.html#) `loads`
method. It decodes datetime values contained in JSON strings: 

```python
    import jsondatetime as json

    >>> test = '{"name": "John Doe", "born": "Thu, 1 Mar 2012 10:00:49 UTC"}'
    >>> json.loads(test)
    {'name': 'John Doe', 'born': datetime.datetime(2012, 3, 1, 10, 0 ,49)}
```
Strings are parsed using `datetime.parser.parse` which is fairly flexible for common datetime formats

## Custom parsing
Being just a wrapper around the `loads` method, you can still use all the standard
`loads` arguments, `object_hook` included. This means that you can still
perform custom parsing of your inbound JSON stream.

## Installation
`pip install json-datetime`
