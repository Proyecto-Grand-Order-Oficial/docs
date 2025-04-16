# Proyecto Grand Order

Este es el repositorio oficial de la documentación del **Proyecto Grand Order**, construido con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## 📂 Estructura del Proyecto

```
├── docs/ # Contenido principal de la documentación 
│ ├── about.md # Página "Acerca de" 
│ ├── index.md # Página principal 
│ ├── assets/ # Recursos estáticos (imágenes, estilos, scripts) 
│ │ ├── logo.svg 
│ │ ├── styles/ 
│ │ │   └── extra.css 
│ │ ├── js/ 
│ │ │   └── extra.js 
│ │ └── theme/ 
│ │     ├── dark/ 
│ │     │   ├── chr.webp 
│ │     │   └── hero.webp 
│ │     └── light/ 
│ │         ├── chr.webp 
│ │         └── hero.webp 
│ ├── blog/ # Blog del proyecto 
│ │ ├── .authors.yml # Información de los autores 
│ │ ├── index.md # Índice del blog 
│ │ └── posts/ 
│ └── assets/overrides/ # Personalizaciones del tema 
│     └── home.html 
├── mkdocs.yml # Configuración de MkDocs 
├── requirements.txt # Dependencias del proyecto 
└── .github/workflows/ # Configuración de CI/CD 
    └── deploy.yml
```


## 🚀 Instalación y Uso

### Requisitos

- Python 3.8 o superior
- `pip` (gestor de paquetes de Python)

### Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Proyecto-Grand-Order-Oficial/docs.git
   cd docs
   ```
2. Instalas los requisitos

    ```bash
    pip install -r requirements.txt
    ```
3. Inicia el servidor de desarrollo

    ```bash
    mkdocs serve
    ```
4. Desarrolla o realiza cambios

### Despliegue

El despliegue se realiza automáticamente a través de GitHub Actions. Para más detalles, consulta el archivo `.github/workflows/deploy.yml`.

## ✨ Características

- Tema: Material for MkDocs
- Blog integrado con soporte para autores y categorías.
- Paleta de colores adaptable (modo claro/oscuro).
- Animaciones personalizadas y diseño responsivo.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para sugerir mejoras.

