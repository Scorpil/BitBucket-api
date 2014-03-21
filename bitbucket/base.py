# -*- coding: utf-8 -*-


class BitbucketApi(object):
    """This class provides base for all API-related classes."""

    URLS = {}
    
    def __init__(self, bitbucket):
        self.bitbucket = bitbucket
        self.bitbucket.URLS.update(self.URLS)

    def _get(self, url_key):
        """ Shortcut for simple GET requests. """
        url = self.bitbucket.url(url_key)
        return self.bitbucket.dispatch('GET', url, auth=self.bitbucket.auth)
