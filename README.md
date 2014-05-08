Socksed
=========

Socksed is small, easy to use decorator for SOCKS proxifying written in Python. On decoration only decorated objects will be executed in proxifyed environment.


For **using**:

  - Install package
  - Open your module
  - Import and enjoy

```sh
git clone https://github.com/Jahangir-Sh/socksed.git
cd socksed
cp -r * [your_project_packages_folder]
```

> **NOTE** For properly working, package must be imported before any network module.

----
Examples of **using**.

```py
from socksed.socksed import *
import urllib

@socksed()
def get_with_socksed(url):
    return urllib.urlopen(url).read()

get_with_socksed('http://ip.jsontest.com/')
```


Default host value is 'localhost', port value is 9150 for using with [tor][1].
Also you can specify other parameters on decorator as demonstrated.
```py
@socksed(port=7052, username='test_user', password='t35t_pa55')
def get_with_socksed_p(url):
    return urllib.urlopen(url).read()
```




**Socksed** uses [SocksiPy][2], an open source project to work properly.



[1]: https://www.torproject.org/ "Tor Project"
[2]: http://socksipy.sourceforge.net/ "SocksiPy"