import os
from box.exceptions import BoxValueError
import yaml
from text_summariser.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return the data
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Read the yaml file from {path_to_yaml } loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise (e)
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories if they don't exist
    """
    for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory: {path}")
        

@ensure_annotations
def get_size(path:Path) -> Any:
    """
    Get the size of the file
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} Kb"