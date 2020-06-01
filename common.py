import yaml


__credentials = None


def credentials():
    global __credentials
    if not __credentials:
        with open('credentials.yaml', mode='r') as f:
            __credentials = yaml.safe_load(f)
    return __credentials
