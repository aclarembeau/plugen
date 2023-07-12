import os
import subprocess
from glob import glob
from pathlib import Path


class Plugin:
    def __init__(self, plugin_config, site_config):
        self.plugin_config = plugin_config
        self.site_config = site_config

    def start(self):
        if not Path(self.site_config['source']).joinpath('tailwind.config.js').exists():
            print('tailwind.config.js file not found, the plugin will not run')

        try:
            subprocess.check_output("npx tailwindcss", shell=True, cwd=self.site_config['source'])
        except Exception as e:
            print(e)
            print('    /!\ unable to run: "npx tailwindcss"')

    def run(self, source_modified, dest_modified):
        reload_tailwind = False
        for file in dest_modified:
            if file.endswith('.html'):
                reload_tailwind = True

        if reload_tailwind:
            css_files = glob('*.css', root_dir=self.site_config['dest'])
            for file in css_files:
                file = Path(self.site_config['dest']).joinpath(file)

                subprocess.check_output('npx tailwindcss -i {0} -o {1}'.format(Path(file).absolute().__str__(),
                                                                               Path(file).absolute().__str__()),
                                        shell=True, cwd=self.site_config['source'])
