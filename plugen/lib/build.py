import os
from shutil import rmtree

from plugen.lib.plugin import plugin_instances
from plugen.lib.utils import read_yaml_file, list_recently_modified_files

def build_func(args):
    print('=== Initialization sequence')
    config = read_yaml_file(args.config)
    instances = plugin_instances(config)

    print('')
    print('=== Building the app')
    build(config, instances)

    print('')
    print('=== Shutdown sequence')
    for instance in instances:
        if hasattr(instance, 'shutdown'):
            instance.shutdown()


def build(config, instances):
    # Implement the build functionality
    print("Building the static website...")
    if os.path.exists(config['dest']):
        rmtree(config['dest'])

    os.mkdir(config['dest'])

    for instance in instances:
        instance.run(
            list_recently_modified_files(config['source'], 0),
            list_recently_modified_files(config['dest'], 0),
        )

