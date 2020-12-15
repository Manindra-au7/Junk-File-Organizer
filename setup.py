# Junk Files Organizer in python

# Importing required libraries
import os
import shutil
from pathlib import Path


DIRECTORIES = {
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"],
    "C++": [".cpp"],
    "C": [".c"],
    "CSS": [".css"],
    "Java": [".jsp", ".jspx", ".wss", ".do", ".action"],
    "JavaScript": [".js"],
    "PHP": [".php", ".php4", ".php3", ".phtml"],
    "SSI": [".shtml"],
    "XML": [".xml", ".rss", ".svg"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  ".pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "TEXT": [".txt", ".in", ".out"],
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"]

}


FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def organise_folder():
    cwd = os.getcwd()
    for entry in os.scandir():
        if not entry.is_dir():
            file_path = os.path.abspath(entry)
            file_format = os.path.splitext(file_path)[1].lower()
            if file_format in FILE_FORMATS:
                directory_path = os.path.join(cwd, "organized")
                if not os.path.exists(directory_path):
                    os.mkdir(directory_path)
                dest_folder = os.path.join(
                    directory_path, FILE_FORMATS[file_format])
                if not os.path.exists(dest_folder):
                    os.mkdir(dest_folder)
                shutil.copy2(file_path, dest_folder)
                dest = os.path.join(dest_folder, entry)
                if os.path.exists(dest):
                    os.remove(file_path)
    try:
        os.mkdir("OTHER - FILES")
    except BaseException:
        pass

    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)),
                          os.getcwd() + '/OTHER - FILES/' + str(Path(dir)))
        except BaseException:
            pass


if __name__ == "__main__":
    organise_folder()
