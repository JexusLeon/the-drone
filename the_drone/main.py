from typing import Final

from fastapi import FastAPI

import versioneer

app: Final = FastAPI(
    debug=True,
    title="The Drone",
    version=versioneer.get_version(),
    description="""Focuses on creating useful functions for drones.""",
)


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: str) -> dict:
    return {"message": f"Hello {name}"}
