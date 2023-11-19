import os
from typing import List

# Opsaetning og import af egne moduler
import sys

sys.path.append(r"C:\Filkassen\PythonMm\VSCode_projects\LIFEOpsaetning")
import partneroversigt as po


def lav_dir(path: str, dirs: List[str]) -> None:
    for dir in dirs:
        new_dir = os.path.join(path, dir)
        os.makedirs(new_dir)
    return


def lav_dir(distr_path, dirs):
    root = r"C:\Temp\TestDir"
    root_dir = "Bilag2023"
    lav_dir(os.path.join(path_root_dir, root_dir), dirs)
    return


def makedir(project):
    match project.lower():
        case "open":
            pass
        case "forfit":
            pass
        case "natman":
            pass
        case "nst":
            pass
        case _:
            print(
                f"{project} er ikke et gyldigt argument - vælg open/forfit/natman/nst"
            )
            return

    return


if __name__ == "__main__":
    makedir("open")
