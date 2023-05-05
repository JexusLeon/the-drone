# The Drone

The project focuses on creating useful functions for drones, such as delivering
small items that are urgently needed in locations with difficult access.

#### Este proyecto utiliza las siguientes herramientas y tecnologías para el desarrollo:

[FastAPI](https://fastapi.tiangolo.com/): A modern, fast web framework for
building Python-based APIs.  
[SQLAlchemy](https://www.sqlalchemy.org/): An object-relational mapping (ORM)
library for Python that makes data manipulation easier and reduces the need to
write SQL manually.  
[Black](https://black.readthedocs.io/en/stable/):  A code formatting tool for
Python that ensures consistent code style throughout the project.  
[Mypy](https://mypy.readthedocs.io): A static type checking tool for Python
that helps detect typing errors before execution.

## Installation

Go inside the folder:

```bash
cd .\the-drone
```

Create a virtual environment for the application:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate.bat
```

- On macOS or Linux:

```bash
source venv/bin/activate
```

Install the application dependencies with pip:

```bash
pip install -r requirements.txt
```

## Run app

```bash
uvicorn the_drone.main:app
```

Access the application docs in your web browser at http://localhost:8000/docs.

## Run test

Install the application dependencies with pip for test:

```bash
pip install -r requirements_dev.txt
```

Then, to run the tests, simply:

```bash
python -m pytest
```
