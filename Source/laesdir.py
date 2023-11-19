import os
from typing import List

# Opsaetning og import af egne moduler
import sys

sys.path.append(r"C:\Filkassen\PythonMm\VSCode_projects\LIFEOpsaetning")
import partneroversigt as po


def laesdir(project):
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
    laesdir("nst")
