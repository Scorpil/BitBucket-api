# -*- coding: utf-8 -*-
from .base import BitbucketApi


class User(BitbucketApi):
    """ This class provide user-related methods to Bitbucket objects. """

    URLS = {
        'GET_USER': 'user/',
        'GET_PRIVS': 'user/privileges/',
        'GET_FOLLOWS': 'user/follows',
        'GET_REPOS': 'user/repositories/',
        'GET_REPOS_OVERVIEW': 'user/repositories/overview/',
        'GET_REPOS_DASH': 'user/repositories/dashboard/',
   }

    def user(self):
        return self._get('USER')

    def privileges(self):
        return self._get('GET_PRIVS')

    def follows(self):
        return self._get('GET_FOLLOWS')

    def repositories(self):
        return self._get('GET_REPOS')

    def overview(self):
        return self._get('GET_REPOS_OVERVIEW')

    def dashboard(self):
        return self._get('GET_REPOS_DASH')
