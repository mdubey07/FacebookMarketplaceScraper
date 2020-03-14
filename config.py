import os


def project_dir():
    filepath = os.path.abspath(__file__)
    main_dir = os.path.dirname(filepath)
    return main_dir
