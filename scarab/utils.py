import os
import urlparse


def url_to_path(url, pubdate):
    urlp = urlparse.urlparse(url)
    m, y = pubdate.split('-')
    return '%s/%s/%s' % (y, m, os.path.basename(urlp.path))
