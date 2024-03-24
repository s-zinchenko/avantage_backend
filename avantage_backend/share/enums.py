import enum


class ReprEnum(enum.Enum):
    def __str__(self):
        return str(self.value)


class IntEnum(int, ReprEnum):
    pass


class StrEnum(str, ReprEnum):
    pass
