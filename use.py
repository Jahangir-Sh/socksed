from socksed.socksed import *

import urllib


def get(url):
    return urllib.urlopen(url).read()


@socksed()
def get_with_socksed(url):
    return urllib.urlopen(url).read()


@socksed(port=7052)
def get_with_socksed_p(url):
    return urllib.urlopen(url).read()

if __name__ == '__main__':
    print get('http://ip.jsontest.com/')
    print get_socksed('http://ip.jsontest.com/')
    print get('http://ip.jsontest.com/')