import logging, re, uuid
import mkdocs.plugins

class GithubEmbedded:
    pattern = r'@Github\((.*?)\)'
    log = logging.getLogger('mkdocs')

    def __init__(self):
        self.pattern = re.compile(self.pattern)

    def extract_repo_from_url(self, url: str) -> str | None:
        match = re.search(r'github\.com/([^/\s]+/[^/\s]+)', url)
        if match:
            return match.group(1)
        self.log.warning(f'No se pudo extraer el repositorio desde la URL: {url}')
        return None

    def generate_open_graph_image(self, repo: str) -> str:
        return f'https://opengraph.githubassets.com/{uuid.uuid4()}/{repo}'

    def generate_embed_html(self, url: str) -> str:
        repo = self.extract_repo_from_url(url)
        if not repo:
            return url  # Devuelve el texto original si no se pudo extraer

        image_url = self.generate_open_graph_image(repo)
        return f'<a href="{url}" target="_blank"><img src="{image_url}" alt="Open Graph image of {repo}" /></a>'

    def replace_match(self, match: re.Match) -> str:
        url = match.group(1).strip()
        return self.generate_embed_html(url)

    def replace_all(self, markdown: str) -> str:
        return self.pattern.sub(self.replace_match, markdown)
    

embed = GithubEmbedded()
@mkdocs.plugins.event_priority(-50)
def on_page_markdown(markdown, page, **kwargs):
    return embed.replace_all(markdown)
