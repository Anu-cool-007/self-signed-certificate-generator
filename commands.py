def createRootCACommand(keyName: str):
    return f"openssl genrsa -des3 -out {keyName}.key 4096"


def createRootCertCommand(keyName: str, certName: str):
    return f"openssl req -x509 -new -nodes -key {keyName}.key -sha256 -days 1024 -out {certName}.crt"


def createCertKeyCommand(domain: str):
    return f"openssl genrsa -out {domain}.key 2048"


def createCsrCommand(domain: str):
    return f"openssl req -new -key {domain}.key -out {domain}.csr"


def createCertCommand(domain: str, keyPath: str, certPath: str):
    return f"openssl x509 -req -in {domain}.csr -CA {certPath} -CAkey {keyPath} -CAcreateserial -out {domain}.crt -days 500 -sha256"


def createPKS12Command(domain: str, alias: str):
    return f"openssl pkcs12 -export -in {domain}.pem -inkey {domain}.key -name {alias} -out {domain}.p12"


def createSha256FingerprintCommand(domain: str):
    return f"openssl x509 -noout -fingerprint -sha256 -inform pem -in {domain}.crt -out {domain}.fingerprint"


def verifyCsrCommand(domain: str):
    return f"openssl req -in {domain}.csr -noout -text"


def verifyCertCommand(domain: str):
    return f"openssl x509 -in {domain}.crt -text -noout"
