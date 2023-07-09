from shutil import copyfile


class Plugin:
    def __init__(self, plugin_config, site_config):
        self.plugin_config = plugin_config
        self.site_config = site_config

    def run(self, source_modified, dest_modified):
        for file in source_modified:
            copyfile(file, file.replace(self.site_config['source'], self.site_config['dest']))
