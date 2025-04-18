import re

import logging, re

log = logging.getLogger('mkdocs')

def on_page_markdown(markdown, **kwargs):
    carousel_pattern = re.compile(r":::carousel\s*\n(.*?)\n:::", re.DOTALL)

    def replace_carousel(match):
        content = match.group(1)
        # Buscar todas las imágenes en formato Markdown dentro del bloque
        image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
        images = image_pattern.findall(content)

        # Construir el HTML del carrusel
        html = ['<div id="carousel" class="flicking-viewport">']
        html.append('  <div class="flicking-camera">')
        
        for src in images:
            html.append('<div class="panel">')
            html.append(f'<img src="/docs/blog/{src}" alt="Image" />')
            html.append('</div>')
        
        html.append('  </div>')
        html.append('</div>')

        return '\n'.join(html)

    # Reemplazar todos los bloques :::carousel ... ::: en el contenido Markdown
    new_markdown = carousel_pattern.sub(replace_carousel, markdown)
    return new_markdown