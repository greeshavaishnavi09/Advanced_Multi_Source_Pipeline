from pathlib import Path

# Current project folder
project_path = Path.cwd() # current working directory i.e., Advanced_Multi_Source_Pipeline

# Folder structure
folders = [
    "data/raw",
    "data/processed",
    "research",
    "src/data_collection",
    "src/data_cleaning",
    "src/feature_engineering",
    "src/visualization",
    "reports/figures",
]

# Files to create
files = [
    "src/__init__.py",
    "src/data_collection/__init__.py",
    "src/data_cleaning/__init__.py",
    "src/feature_engineering/__init__.py",
    "src/visualization/__init__.py",
    "requirements.txt",
    "README.md",
    "main.py",
]

# Create folders
for folder in folders:
    (project_path / folder).mkdir(parents=True, exist_ok=True)

# Create files
for file in files:
    file_path = project_path / file
    file_path.touch(exist_ok=True)

print("Project structure created successfully!")
