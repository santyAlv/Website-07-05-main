# Proyecto Web - Sistema de Gestión de Vehículos
Este proyecto fue desarrollado utilizando el framework Django
y tiene como objetivo gestionar información relacionada con vehículos, conductores y seguimiento de datos dentro de una aplicación web dinámica.

La aplicación cuenta con una estructura organizada mediante aplicaciones, archivos estáticos, plantillas HTML y conexión a base de datos SQLite.

## Tecnologías Utilizadas
- Python 
- Django
- HTML
- CSS
- SQLite
- Visual Studio Code

## Estructura del Proyecto
```bash
    Project/
    │
    ├── Api/
    │   ├── migrations/
    │   ├── static/
    │   │   ├── css/
    │   │   │   └── style.css
    │   │   └── src/
    │   │       ├── car-1.jpg
    │   │       ├── car-2.jpg
    │   │       ├── car-3.jpg
    │   │       ├── driver-1.jpg
    │   │       ├── driver-2.jpg
    │   │       ├── driver-3.jpg
    │   │       └── hero-car.jpg
    │   │
    │   ├── Templates/
    │   │   └── Pages/
    │   │       └── Base.html
    │   │
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── Project/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── db.sqlite3
    ├── manage.py
    └── Readme.md
```

## Instalación del Proyecto
- Clonar el repositorio
```bash
    git clone URL_DEL_REPOSITORIO
```

- Ingresar a la carpeta del proyecto
```bash
    cd Project
```

- Corremos el Servidor
```bash
    python manage.py runserver
```
Aviso Legal
Este proyecto fue desarrollado exclusivamente con fines educativos y de aprendizaje.

Harry Potter, sus personajes, nombres, casas, hechizos, imágenes y demás elementos
relacionados son propiedad intelectual de sus respectivos titulares de derechos. Este
proyecto no tiene fines comerciales ni pretende infringir derechos de autor, marcas
registradas ni cualquier otro derecho de propiedad intelectual.

Todo el contenido utilizado tiene como único propósito la práctica, el aprendizaje y la
demostración de habilidades de desarrollo web mediante Django.

Licencia
Este repositorio se distribuye únicamente con fines educativos y académicos.

No se autoriza el uso comercial de recursos protegidos por derechos de autor que
puedan encontrarse incluidos o referenciados en el proyecto.