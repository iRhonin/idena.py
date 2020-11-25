class IdenaException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __repr__(self):
        return f'Idena RPC Client Exception: {self.code} - {self.message}'
