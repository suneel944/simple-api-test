from enum import Enum, unique

@unique
class Servers(Enum):
    """Available servers"""
    TEST = "test"
    PROD = "prod"
    STAGE = "stage"