
# EGO Challenge

Una app realizada a pedido de la empresa EGO.




## Deployment

Para correr el servidor localmente se debe clonar el repositorio o descargarlo.

```bash
$ git clone https://github.com/ale-demer/ego-challenge.git
$ cd ego-challenge
```

Instalación a través de Pip:

```bash
$ python -m venv .venv
```

Iniciar entorno (Windows): 
```bash
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1
```

Iniciar entorno (macOS): 
```bash
$ source .venv/bin/activate
```

Correr el servidor:
```bash
(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py runserver
```

Se incluye una base de datos con usuario precargado:

- User: test@gmail.com
- Pass: ego
## Features

- Basado en Django 4.2 y Python 3.11
- all-auth, bootstrap5, crispy-forms, SQLite
- Debug toolbar
## FAQ

#### ¿Como creo autos nuevos?

Iniciar sesión. Luego en el menú, presionar el nombre del usuario y en el desplegable elegir "Alta vehículo".

#### ¿Como puedo editar / borrar un auto?

Solo estando logueado, al entrar a la ficha técnica de algún auto aparece en la parte superior una botonera con el ABM para ese vehículo.

#### ¿Como puedo editar / borrar las características o fotos de los autos?

A través del panel de Admin: (localhost:8000/admin).

