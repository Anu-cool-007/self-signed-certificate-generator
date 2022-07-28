
import subprocess
from pathlib import Path
from commands import createCertCommand, createCertKeyCommand, createCsrCommand, createRootCACommand, createRootCertCommand
from model import CertificateDir
from util import getRandomDomain, serchCert, choice
import os


certDir = "./cert/"
rootSubj = "/C=IN/ST=Uttar Pradesh/L=NOIDA/O=Canopus/OU=Canopus Homes/CN=canopushomes.com"


def runProcess(command: str, commandNoSplit: str = "", dir: str = "./"):
    if commandNoSplit != "":
        subprocess.run(command.split(" ") + [commandNoSplit], cwd=dir, shell=True, check=True)
    else:
        subprocess.run(command.split(" "), cwd=dir, shell=True, check=True)


def createDeviceCert(rootCert: CertificateDir):
    randomName = getRandomDomain()
    commonName = input("Enter common name [{rndName}]: ".format(rndName=randomName)) or randomName

    dir = os.path.join(certDir, commonName)
    keyPath = os.path.join(rootCert.path, rootCert.keyName)
    certPath = os.path.join(rootCert.path, rootCert.certName)

    Path(dir).absolute().mkdir(parents=True, exist_ok=True)
    runProcess(command=createCertKeyCommand(domain=commonName), dir=dir)
    runProcess(command=createCsrCommand(domain=commonName), dir=dir)
    runProcess(command=createCertCommand(domain=commonName, keyPath=keyPath, certPath=certPath), dir=dir)


def createRootCert():
    rootName = input("Enter name of root certificate [rootCA] : ") or "rootCA"

    dir = os.path.join(certDir, rootName)
    Path(dir).mkdir(parents=True, exist_ok=True)
    runProcess(command=createRootCACommand(keyName=rootName), dir=dir)
    runProcess(command=createRootCertCommand(keyName=rootName, certName=rootName) +
               " -subj", commandNoSplit=rootSubj, dir=dir)


if __name__ == '__main__':
    if Path('openssl.cnf').is_file():
        os.environ["OPENSSL_CONF"] = str(Path("openssl.cnf").absolute())
        print("Loaded custom ssl conf")
    rootDir = input("Enter dir of root certificate [rootCA] : ") or "rootCA"
    print("Finding Root CA key and certificate")
    rootCert = serchCert(os.path.join(certDir, rootDir))
    if rootCert:
        print(rootCert)
        createDeviceCert(rootCert)
    else:
        choiceLoop = False
        choice = choice("Root certificate not found. Create new one?", 'y', 'n')
        if choice == 'y':
            createRootCert()
            pass
        elif choice == 'n':
            print("Exiting...")
            exit
