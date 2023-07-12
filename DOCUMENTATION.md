# Documentation 

The `plugin.config.yml` file is used to configure the plugins and their options for the Plugen static website generator. This file should be placed in the root directory of your Plugen project.

## Structure

The `plugin.config.yml` file follows a YAML syntax. It consists of the following sections:

1. `source`: Specifies the source directory for your website files.
2. `dest`: Specifies the destination directory where the generated website will be output.
3. `server`: Configures the development server options.
4. `plugins`: Defines the list of plugins and their respective options.

Below is a sample structure of the `plugin.config.yml` file:

```yaml
source: test/source
dest: test/dest

server:
  port: 4567

plugins:
  - name: copydest
    options:
      ignored:
        - tailwind.config.js 
  - name: sass
    options:
      watch: "**/*.scss"
  - name: tailwind
  - name: imagecompressor
  - name: hotreload
```

Let's dive into each section and its properties:

### `source`

The `source` property specifies the directory where your website source files are located. It should be a relative path from the root directory of your project. For example:

```yaml
source: test/source
```

### `dest`

The `dest` property specifies the directory where the generated website files will be output. It should be a relative path from the root directory of your project. For example:

```yaml
dest: test/dest
```

### `server`

The `server` section configures the development server options. It has the following property:

- `port`: Specifies the port number for the development server. If not provided, a default port will be used.

Example:

```yaml
server:
  port: 4567
```

### `plugins`

The `plugins` section defines the list of plugins and their respective options. Each plugin is represented as an item in the list. Each plugin item has the following properties:

- `name`: Specifies the name of the plugin.
- `options`: Provides additional options specific to the plugin.

Example:

```yaml
plugins:
  - name: copydest
    options:
      ignored:
        - tailwind.config.js 
  - name: sass
    options:
      watch: "**/*.scss"
  - name: tailwind
  - name: imagecompressor
  - name: hotreload
```

In the example above, there are five plugins listed: `copydest`, `sass`, `tailwind`, `imagecompressor`, and `hotreload`. Some plugins have additional options specified under the `options` property.

Note: The order of the plugins in the list determines the execution order of the plugins during the website generation process.

That concludes the documentation for the structure of the `plugin.config.yml` file used by Plugen. Make sure to refer to the documentation of each specific plugin for further details on their options and usage.

Feel free to customize the configuration according to your project requirements. Happy static website generation with Plugen!