# -*- coding: utf-8 -*-
from .base import BitbucketApi


class GroupPrivs(BitbucketApi):
    URLS = {
        'GET_GROUP_PRIVS': 'group-privileges/%(accountname)s/',
        'PUT_GROUP_PRIVS': 'group-privileges/%(accountname)s/%(repo_slug)s/%(group_owner)s/%(group_slug)s',
    }

    def get(self, accountname=None):
        if not accountname:
            accountname=self.bitbucket.username
        url = self.bitbucket.url('GET_GROUP_PRIVS', accountname=accountname)
        return self.bitbucket.dispatch('GET', url, auth=self.bitbucket.auth)

    def create(self, repo_slug, group_slug, group_owner=None, accountname=None, privilege='read'):
        url = self.bitbucket.url(
            'PUT_GROUP_PRIVS',
            repo_slug = repo_slug,
            group_slug = group_slug,
            group_owner = group_owner or self.bitbucket.username,
            accountname = accountname or self.bitbucket.username)
        return self.bitbucket.dispatch('PUT', url, auth=self.bitbucket.auth, body=privilege)
