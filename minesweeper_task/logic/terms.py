from enum import IntEnum


class Terms(IntEnum):
    MINE = -1
    EMPTY_FIELD = 0
    NOT_EMPTY_FIELD = 1
    FLAG_ON = 10
    FLAG_OFF = -10
    WIN = 5
