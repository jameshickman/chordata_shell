from chordataweb.server_env import ServerEnvironment


def index(e: ServerEnvironment, s: dict):
    return {}, {'serviceOf': 'json'}