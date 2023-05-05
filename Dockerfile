# Creating a python base with shared environment variables.
FROM python:3.10.11-slim

# Change this for the main app folder.
ENV APP=the_drone

# Setting python gloval variables.
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV PYTHONPATH "$PYTHONPATH:/home"

# Installing and updating necessary applications in linux.
RUN apt-get update && apt-get install -y

# Setting work directory.
ENV APP_PATH=/home/$APP
WORKDIR $APP_PATH

# Setting virtual environment.
ENV VIRTUAL_ENV=$APP_PATH/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Coping requirements and install dependencies.
COPY requirements.txt .
RUN pip3 install --upgrade -r requirements.txt

# Coping the content of the app.
ADD $APP .

CMD exec gunicorn --bind :80 --workers 1 --threads 8 --timeout 0 --worker-class uvicorn.workers.UvicornWorker main:app