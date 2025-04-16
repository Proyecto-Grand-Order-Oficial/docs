from setuptools import setup

setup(
    name='github-repo-media-embed',
    version='0.1',
    py_modules=['plugin'],
    entry_points={
        'mkdocs.plugins': [
            'github-repo-media-embed = plugin:GithubRepoMediaEmbedPlugin',
        ]
    },
)
