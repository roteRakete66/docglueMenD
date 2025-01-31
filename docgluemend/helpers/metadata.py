from pathlib import Path

import yaml
from helpers import languages


def save(etag):
    metadata = {"etag": etag}
    with open(languages.METADATA_FILE, "w", encoding="utf-8") as file:
        yaml.safe_dump(metadata, file)


def load():
    if Path(languages.METADATA_FILE).exists():
        with open(languages.METADATA_FILE, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
