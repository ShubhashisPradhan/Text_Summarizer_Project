import os
import box.exceptions as BoxException
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any 

@ensure_annotations
def read_yaaml(path_to_yaml:Path) -> ConfigBox:
    """Read yaml file and return a ConfigBox object."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxException.BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

#creating directories
@ensure_annotations
def create_directories(path_to_directories: list, versbose=True):
    """ Create directories"""
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if versbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def get_size(path:Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"