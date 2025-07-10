import os
import yaml 
from box.exceptions import BoxValueError
from box import ConfigBox
from src.textsummarizer.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml)as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"successfully {path_to_yaml} loaded")
            return ConfigBox
    except BoxValueError:
        raise ValueError("yaml is emptyy")
    except Exception as e:
        raise e
    
def create_directories(path_to_directories:list,verbose=True):

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
    if verbose:
        logger.info(f"created directory at{path}")