import os
from pathlib import Path

extensions = {
    "DOCUMENTS":[".pdf", ".docx", ".txt",".exe"],
    "AUDIO":[".m4a", ".m4b", ".mp3"], 
    "IMAGES":[".jpg", ".jpeg", ".png"]
}

def pickDir(value):
    for category, ekstensi in extensions.items():
        for suffix in ekstensi:
            if suffix == value:
                return category
    

def organize():
    for items in os.scandir():
        if items.is_dir():
            continue

    filePath = Path(items)
    fileType = filePath.suffix.lower()
    directory = pickDir(fileType)

    if directory == None:
        quit()

    directoryPath = Path(directory)
    if directoryPath.is_dir() != True:
        directoryPath.mkdir()
    filePath.rename(directoryPath.joinpath(filePath))



organize()
