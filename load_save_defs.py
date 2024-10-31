def saveValue(input_value, filedir):
    with open(filedir, 'w') as f:
        f.write(input_value)

def loadValue(filedir):
    with open (filedir, 'r') as f:
        read = f.read()
    return read