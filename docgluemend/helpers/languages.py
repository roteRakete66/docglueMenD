from pathlib import Path

import requests
import yaml
from helpers import metadata

CONFIG_DIR = Path(__file__).parent.parent / "config"
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
LOCAL_LANGUAGES_YML = CONFIG_DIR / "languages.yml"
METADATA_FILE = CONFIG_DIR / "metadata.yaml"
LANGUAGES_YML_URL = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"


def sync():
    stored_etag = metadata.load()
    etag = stored_etag.get("etag")
    headers = {}
    if etag:
        headers["If-None-Match"] = etag
    try:
        response = requests.get(LANGUAGES_YML_URL, headers=headers, timeout=5)
        response.raise_for_status()
        if response.status_code != 304:
            with open(LOCAL_LANGUAGES_YML, "w", encoding="utf-8") as file:
                file.write(response.text)
            metadata.save(response.headers.get("ETag", ""))
    except (requests.RequestException, yaml.YAMLError):
        pass


def load():
    with open(LOCAL_LANGUAGES_YML, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def create_extension_lookup(languages):
    extension_to_language = {}
    for lang, details in languages.items():
        for ext in details.get("extensions", []):
            ext = ext.lstrip(".")
            if ext not in extension_to_language:
                extension_to_language[ext] = lang.lower()
    return extension_to_language


def get_from_extension(file_path, extension_lookup):
    ext = Path(file_path).suffix.lstrip(".")
    return extension_lookup.get(ext, "plaintext")


def get_string(file_path):
    languages = load()
    extension_lookup = create_extension_lookup(languages)
    return get_from_extension(file_path, extension_lookup)
