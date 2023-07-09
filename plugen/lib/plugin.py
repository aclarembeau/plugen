import datetime
import shutil
import tempfile
import zipfile
from pathlib import Path
from pydoc import importfile
from urllib import request


def plugin_instances(config):
    instances = []

    print('Initializing plugins')
    for plugin_config in config['plugins']:
        print('  ' + plugin_config['name'])
        path = Path(__file__).resolve().parent.parent.joinpath(
            'plugins/{0}/plugin.py'.format(str(plugin_config['name']))
        )
        instance = importfile(path.absolute().__str__()).Plugin(plugin_config, config)
        if hasattr(instance, 'start'):
            instance.start()
        instances.append(instance)

    return instances


def list_plugins(args):
    print('==== Listing installed plugins')
    print('')
    print('The installed plugins are: ' )
    print('')
    for path in (list(Path(__file__).parent.parent.glob("plugins/*/plugin.py"))):
        print(' - {0} {1}'.format(path.parent.name.ljust(20), datetime.datetime.fromtimestamp(path.stat().st_mtime)))


def install_plugin(args):
    print('==== installing plugin')
    print('installing plugin', args.name)
    url = 'https://github.com/{0}/archive/refs/heads/master.zip'.format(str(args.name))
    print('looking up for archive', url)

    file = tempfile.mktemp('.zip')
    print('storing archive in', file)
    request.urlretrieve(url, file)

    print('unzipping file')
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(Path(__file__).parent.parent.joinpath('plugins'))

    print('plugin installation done')

def remove_plugin(args):
    print('==== removing plugin')
    plugin_path:Path = Path(__file__).parent.parent.joinpath('plugins/' + args.name)
    if plugin_path.exists():
        print('Removing plugin: ' + args.name)
        shutil.rmtree(plugin_path.__str__())
    else:
        print('The plugin \"{0}\" is not installed'.format(str(args.name)))
        print('Run "list-plugins" to list the available plugins')
