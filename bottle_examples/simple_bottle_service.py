from bottle import Bottle, template


class Server:

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()

    def _route(self):

        """
            Include all the route URL's
        """

        self._app.route('/', method='GET', callback=self._index)
        self._app.route('/hello/<name>', method='GET', callback=self._hello)

    def start(self):

        """
            Start the application with specified host and port
        """

        self._app.run(host=self._host, port=self._port)

    def _index(self):

        """
            On initial page start
        """

        return 'Welcome to bottle'

    def _hello(self, name="Guest"):

        """
            Method to render template
        """

        return template("Hello {{name}}, how are you?", name=name.capitalize())

server = Server(host="localhost", port=8090)
server.start()
