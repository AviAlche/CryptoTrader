
import http.client
import urllib.request
import urllib.parse
import urllib.error

class KrakenConnection(object):
    """ Object representing a single connection.
    Opens a reusable HTTPS connection. Allows specifying HTTPS timeout,
    or server URI (for testing purposes).
    """

    __version__ = '0.1.4'
    __url__ = 'https://github.com/veox/python3-krakenex'

    def __init__(self, uri='api.kraken.com', timeout=30):
        """ Create an object for reusable connections.
        :param uri: URI to connect to
        :type uri: str
        :param timeout: blocking operations' timeout (in seconds)
        :type timeout: int
        :returns: None
        """
        self.headers = {
            'User-Agent': 'krakenex/' + self.__version__ +
            ' (+' + self.__url__ + ')'
        }
        self.conn = http.client.HTTPSConnection(uri, timeout=timeout)
        return

    def close(self):
        """ Close this connection.
        :returns: None
        """
        self.conn.close()
        return

    def _request(self, url, req=None, headers=None):
        """ Send POST request to API server using this connection.
        If not provided, sets empty request parameters and HTTPS
        headers for this request.
        :param url: fully-qualified URL with all necessary urlencoded
             information
        :type url: str
        :param req: (optional) API request parameters
        :type req: dict
        :param headers: (optional) HTTPS headers, such as API-Key and API-Sign
        :type headers: dict
        :returns: :py:mod:`http.client`-decoded response
        :raises: :py:exc:`http.client.HTTPException`: if response status not
             successful
        """

        if req is None:
            req = {}

        if headers is None:
            headers = {}

        data = urllib.parse.urlencode(req)
        headers.update(self.headers)

        self.conn.request('POST', url, data, headers)
        response = self.conn.getresponse()

        if response.status not in (200, 201, 202):
            raise http.client.HTTPException(response.status)

        return response.read().decode()