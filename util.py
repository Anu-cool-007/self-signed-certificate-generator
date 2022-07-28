from pathlib import Path
import secrets
import string
import os

from model import CertificateDir


def choice(statement: str, *choices: str):
    while(True):
        choice = input(statement+" [" + ','.join(choices) + "]: ")
        if choice in choices:
            return choice
        else:
            print("Invalid option\n")
			
def serchCert(dir: str) -> CertificateDir:
    certDir = Path(dir).absolute()
    if certDir.is_dir():
        certPath = certDir.joinpath(certDir.name + ".crt")
        keyPath = certDir.joinpath(certDir.name + ".key")
        if certPath.is_file() and keyPath.is_file():
            return CertificateDir(path=certDir, keyName=keyPath.name, certName=certPath.name)


def getRandomDomain(length: int = 10):
    return ''.join(secrets.choice(string.ascii_lowercase + string.digits) for i in range(length)) + ".com"
