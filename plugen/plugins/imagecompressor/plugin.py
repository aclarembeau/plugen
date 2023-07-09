class Plugin:
    def __init__(self, plugin_config, site_config):
        self.plugin_config = plugin_config
        self.site_config = site_config

    def run(self, source_modified, dest_modified):
        pass