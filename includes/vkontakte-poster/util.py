import urllib, requests, re
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen, Request
from httplib2 import iri2uri
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"

def curl_get(url, data = {}):
	newUrl = iri2uri(url)+"?"+urlencode(data)
	return urlopen(newUrl).read()

def curl_post(url, data = {}):
	url = iri2uri(url)
	data = urlencode(data).encode("utf-8")
	return urlopen(Request(url, data)).read()

def curl_fetch_binary(url, data = None):
	url = iri2uri(url)
	req = Request(url, data=data, headers={'User-Agent': userAgent, "Accept-Language": "en"})
	with urlopen(req) as f:
		data = f.read()
	return data

def download_url(url, filename, data = {}):
	with open(filename, 'wb') as f:
		f.write(curl_fetch_binary(url, data))

def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)
