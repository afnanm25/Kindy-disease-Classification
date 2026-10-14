import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """يقوم بقراءة ملف yaml وإرجاع محتواه كـ ConfigBox

    Args:
        path_to_yaml (Path): مسار ملف yaml

    Raises:
        ValueError: إذا كان ملف yaml فارغاً
        e: أي خطأ آخر أثناء القراءة

    Returns:
        ConfigBox: البيانات المقروءة بتنسيق ConfigBox
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """إنشاء قائمة من المجلدات

    Args:
        path_to_directories (list): قائمة تحتوي مسارات المجلدات
        verbose (bool, optional): طباعة سجل التشغيل. يتخلف إلى True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """حفظ البيانات في ملف json

    Args:
        path (Path): مسار حفظ الملف
        data (dict): البيانات المراد حفظها
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """تحميل البيانات من ملف json

    Args:
        path (Path): مسار ملف json

    Returns:
        ConfigBox: البيانات محملة كعناصر قابلة للوصول بواسطة النقطة (.)
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """حفظ ملف ثنائي (Binary)

    Args:
        data (Any): البيانات المراد حفظها
        path (Path): مسار الحفظ
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """تحميل ملف ثنائي

    Args:
        path (Path): مسار الملف الثنائي

    Returns:
        Any: البيانات المخزنة داخل الملف
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """حساب حجم الملف بالكيلوبايت

    Args:
        path (Path): مسار الملف

    Returns:
        str: حجم الملف بالكيلوبايت
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    """فك تشفير صورة بصيغة Base64 وحفظها كملف صورة"""
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """تحويل ملف صورة إلى نص مشفر بصيغة Base64"""
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())