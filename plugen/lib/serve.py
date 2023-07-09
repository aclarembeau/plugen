import http.server
import math
import os
import socketserver
import threading
import time
from functools import partial
from shutil import rmtree

from plugen.lib.plugin import plugin_instances
from plugen.lib.utils import list_recently_modified_files, read_yaml_file

killed = False


def serve_func(args):
    print('=== Initialization sequence')
    config = read_yaml_file(args.config)
    instances = plugin_instances(config)

    print('')
    print('=== Running the server')
    serve(config, instances)

    print('')
    print('=== Shutdown sequence')
    for instance in instances:
        if hasattr(instance, 'shutdown'):
            instance.shutdown()

def thread_function(config, instances):
    global killed
    before_all_plugins = 0

    while not killed:
        files_changed = list_recently_modified_files(config['source'], before_all_plugins)
        if files_changed:
            print('')
            print(str(len(files_changed)) + ' file(s) changed')

        if files_changed:

            for instance in instances:
                before_this_plugin = time.time()

                print('   running plugin: ' + instance.plugin_config['name'].ljust(30), end='...')

                source_modified = list_recently_modified_files(config['source'], before_all_plugins)
                dest_modified = list_recently_modified_files(config['dest'], before_all_plugins)
                instance.run(
                    source_modified,
                    dest_modified,
                )

                print('   execution time: ' + str(math.floor((time.time()-before_this_plugin))) + 'ms')


            before_all_plugins = time.time()
        time.sleep(0.3)

    return True

def serve(config, instances):
    global killed
    port = (config['server']['port'])

    handler = partial(http.server.SimpleHTTPRequestHandler, directory=config['dest'])
    with socketserver.TCPServer(("localhost", port), handler) as httpd:
        # Implement the serve functionality
        print("Serving on http://localhost:{0}".format(str(port)))

        if os.path.exists(config['dest']):
            rmtree(config['dest'])
        os.mkdir(config['dest'])

        httpd.allow_reuse_address = True
        httpd.directory = config['dest']
        thread = threading.Thread(target=thread_function, args=(config, instances))

        thread.start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()

        killed = True
        thread.join()

