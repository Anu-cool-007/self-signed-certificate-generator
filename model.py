from dataclasses import dataclass
from typing import List


@dataclass
class CertificateDir:
    path: str
    keyName: str
    certName: str
