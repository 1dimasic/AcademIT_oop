from enum import IntEnum


class Terms(IntEnum):
    GAME_OVER = -100
    MINE = -1
    WIN = 100
    FLAG_ON = 5
    FLAG_OFF = -5
