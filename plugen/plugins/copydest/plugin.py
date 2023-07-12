from pathlib import Path
from shutil import copyfile


class Plugin:
    def __init__(self, plugin_config, site_config):
        self.plugin_config = plugin_config
        self.site_config = site_config

    def run(self, source_modified, dest_modified):
        for source_file in source_modified:
            ignored = False

            dest_file = source_file.replace(self.site_config['source'], self.site_config['dest'])
            for ignored_pattern in self.plugin_config['options']['ignored']:
                if Path(source_file).match(ignored_pattern):
                    ignored = True

            if not ignored:
                copyfile(source_file, dest_file)
