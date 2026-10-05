import unittest, socket, concurrent.futures
from app.web_api.server import ChatHTTPServer, ChatHandler

class NativeBurstIntakeTests(unittest.TestCase):
    def test_ten_pending_connections_reach_native_intake(self):
        server=ChatHTTPServer(('127.0.0.1',0),ChatHandler)
        clients=[]
        def connect(_):
            client=socket.socket();client.settimeout(1)
            try:client.connect(server.server_address);return client
            except Exception:client.close();raise
        try:
            # No accept loop yet: all ten must fit while the server is busy.
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
                futures=[pool.submit(connect,i) for i in range(10)]
                for future in futures:
                    try:clients.append(future.result())
                    except OSError as exc:self.fail(str(exc))
            self.assertEqual(len(clients),10)
        finally:
            for client in clients:client.close()
            server.server_close()
