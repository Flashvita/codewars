""""
Write a function that when given a URL as a string,
parses out just the domain name and returns it as a string. For example:
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cne
"""

from urllib.parse import urlsplit


def domain_name(url):
    return urlsplit(url).hostname.partition('.')[0]


print(domain_name('http://google.com'))