def test(_Class):
    instance = _Class()
    instance.method()
    print(instance.staticAttribute)
    print(instance.method())
    print(instance.staticAttribute)
    try:
        print(instance.action())
    except:
        pass
    try:
        print(instance.delegate())
    except:
        pass
    print('\n')
