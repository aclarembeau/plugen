import argparse

from plugen.lib import build_func, serve_func
from plugen.lib.plugin import list_plugins, install_plugin, remove_plugin


def main():
    parser = argparse.ArgumentParser(prog='plugen', description='Pluggable static website generator')

    # Subparsers for the different commands
    subparsers = parser.add_subparsers(title='commands', dest='command')
    subparsers.required = True

    # Build command
    build_parser = subparsers.add_parser('build', help='Build the static website')
    build_parser.add_argument('-c', '--config', help='Specify a configuration file', default='plugen.config.yml')
    build_parser.set_defaults(func=build_func)

    # Serve command
    serve_parser = subparsers.add_parser('serve', help='Serve the static website locally')
    serve_parser.add_argument('-c', '--config', help='Specify a configuration file', default='plugen.config.yml')
    serve_parser.set_defaults(func=serve_func)

    # Plugins command
    list_parser = subparsers.add_parser('list-plugins', help='List the available plugins')
    list_parser.set_defaults(func=list_plugins)
    install_parser = subparsers.add_parser('add-plugin', help='Install a plugin')
    install_parser.add_argument('name', help='The name of the plugin to install')
    install_parser.set_defaults(func=install_plugin)
    remove_parser = subparsers.add_parser('remove-plugin', help='Remove a plugin')
    remove_parser.add_argument('name', help='The name of the plugin to remove')
    remove_parser.set_defaults(func=remove_plugin)

    # Optional flag to specify a configuration file
    args = parser.parse_args()

    # Call the appropriate function based on the chosen command
    args.func(args)


if __name__ == '__main__':
    main()
