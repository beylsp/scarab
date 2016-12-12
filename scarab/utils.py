import os
import urlparse


def url_to_path(url):
    # http://media.motorsportmagazine.com/archive/january-1977/full/27.jpg
    # --> 1977/january/27.jpg
    try:
        urlp = urlparse.urlparse(url)
        dirname, name = os.path.split(urlp.path)
        pubdate = dirname.split('/')[2]
        m, y = pubdate.split('-')
        return '%s/%s/%s' % (y, m, name)
    except Exception, err:
        raise ValueError(err)
