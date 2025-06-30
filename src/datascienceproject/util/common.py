import os        # file and dir ops
import yaml      # r/w yaml files
from src.datascienceproject import logger       # custome logging src.datascienceproject
import json                                     # r/w json files
import joblib                                   # save model persistence in hard disk joblib format
from ensure import ensure_annotations           # decorator - func() runtime dtype
from box import ConfigBox                       # python-box class access
from pathlib import Path                        # data handling
from typing import Any                          # generic type support
from box.exceptions import BoxValueError        # exception handling - parse empty or bad in ConfigBox

print("Reads a YAML file and returns its contents as an object with dot-access")

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            # ✅ convert all string paths to Path objects if needed
            def convert_paths(obj):
                if isinstance(obj, dict):
                    return ConfigBox({k: convert_paths(Path(v) if isinstance(v, str) and ('/' in v or '\\' in v) else v) for k, v in obj.items()})
                return obj

            converted = convert_paths(content)

            logger.info(f"yaml file :{path_to_yaml} loaded successfully")
            return converted

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

print("Run successfully")

print("more yaml generic functions create")

print("Creates one or more directories. Automatically skip existing ones")

@ensure_annotations
def create_directories(path_to_directories:list, verbose:bool=True):
    """
    Args:
        path to directories (list) : list of path of directories
        ignore_log (bool, optional) : ignore if multiple dirs is to be created . Defaults to 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")


print("Saves a dictionary as a .json file. Metadata , Predictions , Evaluations")
@ensure_annotations
def sav_json(path:Path, data:dict):
    """
    save json data

    Args :
        path(Path) : path to json file
        data(dict) : data to be saved as json file
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at:{path}")

print("Loads a .json file and returns a ConfigBox (dot-accessible dict).")
@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """
    load json files data

    Args:
        path(Path) : path to json file
        ConfigBox : data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from :{path}")
    return ConfigBox(content)

print("Saves Any Python object (model, list, dictionary, etc.) to a file in binary format.")
@ensure_annotations
def save_bin(data: Any, path:Path):
    """
    save binary file

    Args:
    data(Any): data to be saved as binary 
    path(Path): path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at:{path}")

print("Loads the binary file and returns the original Python object.")
@ensure_annotations
def load_bin(path:Path)-> Any:
    """
    load binary data

    Args:
        path(Path): path to binary files
    Returns: 
        Any object stored in the file

    """
    data = joblib.load(path)
    logger.info(f"binaryfile loaded at:{path}")
    return data

# "dump" here means: write the object to disk in binary format.
# Creates a .pkl or .joblib file depending on extension

'''
THIS UTILITIES FUNTIONS 

They standardize repetitive tasks like 
reading configs, saving models, managing folders, and logging 
— which allows your training, evaluation, and deployment workflows 
to run consistently and automatically in pipelines or CI/CD tools.


'''