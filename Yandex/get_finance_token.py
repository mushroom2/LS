import hashlib


def f_t(method, number):
    masterToken = 'Sd55LnMcmyCedGy8'
    operationNum = number
    usedMethod = method
    login = 'python-avi'
    financeToken = hashlib.sha256(masterToken + str(operationNum) + usedMethod + login).hexdigest()
    return str(financeToken)

