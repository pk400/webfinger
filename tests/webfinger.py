import unittest

from starlette.testclient import TestClient

from webfinger import app

class TestWebfinger(unittest.TestCase):
  def test_asgi(self):
    client = TestClient(app, base_url='https://testserver')
    response = client.get('/webfinger?resource=a')
    self.assertEqual(response.status_code, 404)
    response = client.get('/.well-known/webfinger?resource=a')
    self.assertEqual(response.status_code, 200)
  
  def test_ssl(self):
    client = TestClient(app)
    response = client.get('/.well-known/webfinger?resource=a')
    self.assertEqual(response.status_code, 495)
  
  def test_valid_query(self):
    client = TestClient(app, base_url='https://testserver')
    response = client.get('.well-known/webfinger')
    self.assertEqual(response.status_code, 400)
    response = client.get('/.well-known/webfinger?resource=a&rel=b')
    self.assertEqual(response.status_code, 200)
    response = client.get('/.well-known/webfinger?resource=a&rel=b&rel=c')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
  unittest.main()