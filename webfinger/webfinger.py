from starlette.endpoints import HTTPEndpoint
from starlette.responses import Response

from .jrd import JRD

class WebFingerEndpoint(HTTPEndpoint):
  '''RFC7033 compliant WebFinger implementation.'''

  async def get(self, request):
    if request['scheme'] != 'https':
      return Response(status_code=495)
    params = request.query_params
    if 'resource' not in params:
      return Response(status_code=400)
    if 'rel' in params:
      rels = []
      for x in params.getlist('rel'):
        rels.append(('rel', x))
    return self._process_request(params['resource'], rels)
    
  def process_request(self, resource, rels):
    '''Override process_request to retrieve the requested resource.
    
    Args:
      resource (str): Resource parameter.
      rels (list): List of link relation objects.
    
    Returns:
      JRD object.
    '''
    raise NotImplementedError()
  
  def _process_request(self, resource, rels):
    response = self.process_request(resource, rels)
    if not isinstance(JRD):
      return Response('Response is not a JRD.', status_code=500)
    return response.response()

