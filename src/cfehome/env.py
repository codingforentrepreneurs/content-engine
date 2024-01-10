import os
import pathlib
from functools import lru_cache
from decouple import Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).parent.parent
ROOT_DIR = BASE_DIR.parent
ENV_FILE_NAME = os.environ.get("ENV_FILE") or ".env"
ENV_BASE_DIR = BASE_DIR / ENV_FILE_NAME
ENV_ROOT_DIR = ROOT_DIR / ENV_FILE_NAME

@lru_cache
def get_config():
    if ENV_BASE_DIR.exists():
        return Config(
            RepositoryEnv(str(ENV_BASE_DIR))
        )
    if ENV_ROOT_DIR.exists():
        return Config(
            RepositoryEnv(str(ENV_ROOT_DIR))
        )
    from decouple import config
    return config

config = get_config()