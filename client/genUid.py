import uuid

def genUdis():
    codegentrated = str(uuid.uuid4()).replace('-', "")[:33]
    return codegentrated
def referCode():
    codes = str(uuid.uuid4()).replace('-', "")[:8]
    return codes
def depositeGenId():
    codes = str(uuid.uuid4()).replace('-', "")[:8]
    return codes
