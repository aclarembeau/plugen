import os
import subprocess


class Plugin:
    def __init__(self, plugin_config, site_config):
        self.plugin_config = plugin_config
        self.site_config = site_config

    def start(self):
        try:
            subprocess.check_output("npx sass --version", shell=True)
        except Exception as e:
            print(e)
            print('    /!\ unable to run: "npx sass"')

    def run(self, source_modified, dest_modified):
        os.system('npx sass ' + self.site_config['source'] + ':' + self.site_config['dest'])