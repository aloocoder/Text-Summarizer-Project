import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format=  '[%(asctime)s]: %(message)s:')

project_name = "Text-Summarizer"

list_of_files = [
    ".github/workflows/.gitkeep" ##needed during deployment, the .gitkeep is a temp file so initial commit is not an empty folder --> later will be changed to some .yml file
    f"src/{project_name}/__init__.py", ##install it as a package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "conifg/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath) ## identifies the os and converts the file path in suitble foem
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"created directiory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty filepath: {filepath}")

    else:
        logging.info(f"{filename} already exists")
