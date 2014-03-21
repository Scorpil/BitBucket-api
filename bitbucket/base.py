# -*- coding: utf-8 -*-


class BitbucketApi(object):
    """This class provides base for all API-related classes."""

    URLS = {}
    
    def __init__(self, bitbucket):
        self.bitbucket = bitbucket
        self.bitbucket.URLS.update(self.URLS)
