Plugen allows you to extend its functionality by creating custom plugins. Plugins are written in Python and can be installed into Plugen using a URL to a zip archive containing the plugin code.

## Plugin Structure

A custom plugin for Plugen follows a specific structure. Here's an example structure for a custom plugin:

```python
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
            print('    /!\\ unable to run: "npx sass"')

    def run(self, source_modified, dest_modified):
        os.system('npx sass ' + self.site_config['source'] + ':' + self.site_config['dest'])
```

Let's break down the different components of the plugin:

- The `Plugin` class represents the custom plugin. It should have the same name as the Python file.
- The `__init__` method is the plugin's constructor. It receives two arguments: `plugin_config` and `site_config`. These arguments provide the plugin-specific configuration and the global site configuration, respectively.
- The `start` method is called when the plugin is started. It is typically used for initialization tasks or checks before running the plugin logic.
- The `run` method is the main logic of the plugin. It is called when Plugen processes the source files and prepares the generated website. You can define your custom logic within this method, using the provided `source_modified` and `dest_modified` arguments if necessary. Those contains the list of files modified in the source, and in the destination directory

## Packaging and Installation

To install a custom plugin into Plugen, you need to package it into a zip archive and provide the URL to the archive during the installation process.

1. Create a new directory for your plugin and place the Python file(s) inside it.
2. Create a zip archive of the plugin directory. Make sure to preserve the directory structure.
3. Upload the zip archive to a publicly accessible location, such as a file hosting service or version control repository.
4. Open a terminal or command prompt and run the following command to install the plugin:

```bash
plugen install URL.zip
```

Replace `URL.zip` with the actual URL of the zip archive you uploaded.

After the installation is complete, Plugen will be able to use the functionalities provided by your custom plugin.

## Conclusion

Creating a custom plugin for Plugen allows you to extend the capabilities of the static website generator according to your specific needs. By following the plugin structure and packaging guidelines, you can easily integrate your custom logic into Plugen's workflow.

Refer to the Plugen documentation for further information on plugin development and usage.

Happy plugin development with Plugen!