def validator(functionName, paramLength):
    # keyが関数名、valueが関数名と必要な引数の数(引数がない関数に対応するために、必ず1以上になるようにする)
    functions = {"reverse": 3, "copy": 3, "dupulicate-contents": 3, "replace-string": 4}
    if functionName.lower() not in functions or functions[functionName] != paramLength:
        return False
    
    return True
