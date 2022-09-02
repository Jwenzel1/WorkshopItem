from enum import Enum


class AutoNameEnum(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self.replace("_", " ").title()

    def __str__(self) -> str:
        return self.value
