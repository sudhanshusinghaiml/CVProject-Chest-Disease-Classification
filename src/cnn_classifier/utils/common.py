"""This module consists of all utility functions for reading/saving the data or config files"""

import os
import json
import base64
from pathlib import Path
from typing import Any
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from src.cnn_classifier.logger import logging


@ensure_annotations
def read_yaml(yaml_file_path: Path) -> ConfigBox:
    """
    Args:
        yaml_file_path (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        if get_size(yaml_file_path) != 0:
            with open(yaml_file_path, "rb") as yaml_file:
                file_content = yaml.safe_load(yaml_file)
            logging.info("YAML file - %s loaded successfully", yaml_file_path)
        else:
            logging.error("YAML file - %s is empty", yaml_file_path)
            raise ValueError(f"YAML file {yaml_file_path} is empty")

        return ConfigBox(file_content)

    except Exception as error:
        logging.error("Exception in utils.common.read_yaml function \n %s", error)
        raise error


@ensure_annotations
def create_directories(directory_list: list, verbose=True):
    """
    Args:
        directory_list (list): list of path of directories
        verbose (bool, optional): ignore if multiple dirs is to be created. Defaults to True.

    """
    try:
        for directory in directory_list:
            os.makedirs(directory, exist_ok=True)
            if verbose:
                logging.info("created directory at: %s", directory)
    except Exception as error:
        logging.error(
            "Exception in utils.common.create_directories function:\n %s", error
        )
        raise error


@ensure_annotations
def save_json(json_file_path: Path, data: dict):
    """save json data

    Args:
        json_file_path (Path): path to json file
        data (dict): data to be saved in json file
    """
    try:
        with open(json_file_path, "wb", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        logging.info("JSON file saved at: %s ", json_file_path)
    except Exception as error:
        logging.error("Exception in utils.common.save_json function \n %s", error)
        raise error


@ensure_annotations
def load_json(json_file_path: Path) -> ConfigBox:
    """load json files data

    Args:
        json_file_path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    try:
        with open(json_file_path, "rb") as json_file:
            data = json.load(json_file)

        logging.info("JSON file loaded succesfully from: %s", json_file_path)

        return ConfigBox(data)
    except Exception as error:
        logging.error("Exception in utils.common.load_json function \n %s", error)
        raise error


@ensure_annotations
def save_bin(data: Any, file_path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        file_path (Path): path to binary file
    """
    try:
        joblib.dump(value=data, filename=file_path)
        logging.info("binary file saved at: %s", file_path)
    except Exception as error:
        logging.error("Exception in utils.common.save_bin function \n %s", error)
        raise error


@ensure_annotations
def load_bin(file_path: Path) -> Any:
    """load binary data

    Args:
        file_path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    try:
        data = joblib.load(file_path)
        logging.info("Binary file loaded from: %s", file_path)
        return data
    except Exception as error:
        logging.error("Exception in utils.common.load_bin function \n %s", error)
        raise error


@ensure_annotations
def get_size(file_path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    try:
        size_in_kb = round(os.path.getsize(file_path) / 1024)
        return f"~ {size_in_kb} KB"
    except Exception as error:
        logging.error("Exception in utils.common.get_size function \n %s ", error)
        raise error


def decode_image(image_string: str, file_name: Path) -> None:
    """Function to decode the image."""
    try:
        imgdata = base64.b64decode(image_string)
        with open(file_name, "wb") as file:
            file.write(imgdata)
            file.close()
    except Exception as error:
        logging.error("Exception in utils.common.decode_image function \n %s", error)
        raise error


def encode_image_into_base64(cropped_image_path: Path) -> bytes:
    """Function to encode the image in base64"""
    try:
        with open(cropped_image_path, "rb") as file_name:
            return base64.b64encode(file_name.read())
    except Exception as error:
        logging.error(
            "Exception in utils.common.encode_image_into_base64 function \n %s", error
        )
        raise error
