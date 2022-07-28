def createRootCACommand(keyName: str):
    return "openssl genrsa -des3 -out {keyName}.key 4096".format(keyName=keyName)


def createRootCertCommand(keyName: str, certName: str):
    return "openssl req -x509 -new -nodes -key {keyName}.key -sha256 -days 1024 -out {certName}.crt" \
        .format(keyName=keyName, certName=certName)


def createCertKeyCommand(domain: str):
    return "openssl genrsa -out {domain}.key 2048".format(domain=domain)


def createCsrCommand(domain: str):
    return "openssl req -new -key {domain}.key -out {domain}.csr".format(domain=domain)


def createCertCommand(domain: str, keyPath: str, certPath: str):
    return "openssl x509 -req -in {domain}.csr" \
        " -CA {certPath} -CAkey {keyPath}" \
        " -CAcreateserial -out {domain}.crt -days 500 -sha256" \
        .format(domain=domain, certPath=certPath, keyPath=keyPath)


def verifyCsrCommand(domain: str):
    return "openssl req -in {domain}.csr -noout -text".format(domain=domain)


def verifyCertCommand(domain: str):
    return "openssl x509 -in {domain}.crt -text -noout".format(domain=domain)
