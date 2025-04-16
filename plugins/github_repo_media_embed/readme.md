# GitHub Repo Media Embed Plugin for MkDocs

`github-repo-media-embed` is a MkDocs plugin that downloads OpenGraph images from GitHub repositories and saves them into a specified folder. This plugin is useful for embedding repository images in your documentation.

## Features

- Automatically fetches OpenGraph images from GitHub repositories.
- Saves images to a specified folder for easy access.
- Default download folder: `/docs/assets/images/github-embed`.

## Installation
No uploaded plugin install on local with -e


## Configuration

Add the plugin to your `mkdocs.yml` configuration file:

```yaml
plugins:
    - github-repo-media-embed:
            download-folder: /path/to/your/folder  # Optional, default is /docs/assets/images/github-embed
```

### Options

- `download-folder`: Specifies the folder where the images will be saved. Defaults to `/docs/assets/images/github-embed`.

## Usage

Once configured, the plugin will automatically download OpenGraph images for GitHub repositories referenced in your documentation. The images will be saved in the specified folder.

## Example

If you reference a GitHub repository in your documentation, the plugin will fetch its OpenGraph image and save it:

```markdown
@Github(assets/images/github-embed/repo-name.png)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/yourusername/github-repo-media-embed).

## Support

For questions or issues, please open an issue on the [GitHub repository](https://github.com/yourusername/github-repo-media-embed).