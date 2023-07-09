import os
import threading
import time

import websockets

import websockets.sync.server

script = '''
<script type="text/javascript">
function connect(){
    let socket = new WebSocket("ws://localhost:8001");
    
    socket.onmessage = function(event) {
      window.location.reload()
    };
    
    socket.error = function(event){
        connect()
    }
}

connect()
</script>
'''


class Plugin:
    def __init__(self, plugin_config, site_config):
        self.plugin_config = plugin_config
        self.site_config = site_config
        self.clients = []

        def listen():
            with websockets.sync.server.serve(handler, "localhost", 8001) as server:
                self.server = server
                server.serve_forever()

        def handler(websocket):
            try:

                print('Websocket client connected')
                self.clients.append(websocket)
                while True:
                    websocket.recv()
            except:
                print('Client disconnected')

        thread = threading.Thread(target=listen, args=())
        thread.start()

    def shutdown(self):
        self.server.shutdown()

    def run(self, source_modified, dest_modified):
        with open(os.path.join(self.site_config['dest'], 'version'), 'w+') as f:
            f.write(str(time.time()))

        for file in dest_modified:
            with(open(file, 'r') as f):
                content = f.read()

            if 'head' in content and script not in content:
                with(open(file, 'w+') as f):
                    content = content.replace('<head>', '<head>'  + script)
                    f.write(content)

        for client in self.clients:
            try:
                client.send('reload')
            except:
                self.clients.remove(client)