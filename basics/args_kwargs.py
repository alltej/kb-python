def array_message(*argv):
    for arg in argv:
        print(arg)


def keyval_message(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


def main():
    array_message("hello there!", "How are you?", "Glad to meet you")
    kwargs = {"arg1": "john", "arg2": "22", "arg3": "Roswell", "arg4": "male"}
    keyval_message(**kwargs)


if __name__ == '__main__':
    main()
