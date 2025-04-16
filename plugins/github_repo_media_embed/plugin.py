from mkdocs.plugins import BasePlugin
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
from mkdocs.config.config_options import Type

import xml.etree.ElementTree as etree
import re
import os
import hashlib
import requests

class GithubEmbedInlineProcessor(InlineProcessor):
    def __init__(self, pattern, md, dest_dir):
        super().__init__(pattern, md)
        self.dest_dir = dest_dir

    def download_image(self, repo):
        # Generate a random hash for the image
        random_hash = hashlib.sha256(os.urandom(32)).hexdigest()

        # Download OpenGraph image
        remote_url = f"https://opengraph.githubassets.com/{random_hash}/{repo}"
        resp = requests.get(remote_url, timeout=10)

        if resp.status_code != 200:
            return None

        # Create destination directory if it doesn't exist
        os.makedirs(self.dest_dir, exist_ok=True)

        # Save image with repo name
        filename = f"{repo.replace('/', '-')}.png"
        dest_path = self.dest_dir + "/" + filename
        
        with open(dest_path, 'wb') as f:
            f.write(resp.content)

        return dest_path

    def handleMatch(self, m, data):
        url = m.group(1)
        match = re.search(r'github\.com/([^/]+/[^/]+)', url)

        if not match:
            return None, m.start(0), m.end(0)

        repo = match.group(1)

        # Check if image already exists to avoid downloading again
        filename = f"{repo.replace('/', '-')}.png"
        dest_path = self.dest_dir + "/" + filename

        if not os.path.exists(dest_path):
            dest_path = self.download_image(repo)
            
            if not dest_path:
                return None, m.start(0), m.end(0)

        # Create an image element with relative path
        img = etree.Element('img')
        img.set('src', "/" + dest_path)
        img.set('class', 'github-embed')
        img.set('alt', repo)


        # Create a link element
        link = etree.Element('a')
        link.set('href', url)
        link.set('target', '_blank')
        link.set('class', 'github-embed-wrapper')
        link.set('rel', 'noopener noreferrer')
        link.append(img)

        return link, m.start(0), m.end(0)

class GithubEmbedExtension(Extension):
    def __init__(self, **kwargs):
        self.dest_dir = kwargs.pop('dest_dir')
        super().__init__(**kwargs)
    
    def extendMarkdown(self, md):
        pattern = r'@Github\((.*?)\)'
        md.inlinePatterns.register(
            GithubEmbedInlineProcessor(pattern, md, self.dest_dir),
            'github-embed', 175
        )


class GithubRepoMediaEmbedPlugin(BasePlugin):
    config_scheme = (
        # ruta relativa dentro de `docs/` donde guardar las imágenes
        ('download-folder', Type(str, default='docs/assets/images/github-embed')),
    )
    
    def on_config(self, config):
        # registra la extensión pasándole `dest_dir`
        config['markdown_extensions'].append(
            GithubEmbedExtension(dest_dir=self.config['download-folder'])
        )
        return config
