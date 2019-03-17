import requests
from urllib.parse import urlparse, urlunparse

class Webfinger:
  def find_account(self, acct_uri):
    components = urlparse(acct_uri)
    if components.scheme != 'acct':
      print('Not an acct URI.')
    userpart, host = components.path.split('@')
    response = self._get_account_from_host(host, userpart)
    if response.status_code == 200:
      return response.json()
    return None

  def _get_account_from_host(self, host, userpart):
    acct_uri = 'resource=acct:{}@{}'.format(userpart, host)
    return requests.get(urlunparse((
      'https', host, '/.well-known/webfinger', None, acct_uri, None)))

