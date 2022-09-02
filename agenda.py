from typing import Sequence, List, Deque
from collections import deque

from workshop_item import WorkshopItem


class Agenda:
    @classmethod
    def get_all_agendas_for_item(
        cls, starting_item: WorkshopItem, hours_remaining=0
    ) -> Sequence["Agenda"]:
        agendas: List[Agenda] = []
        final_item = False
        total_hours = starting_item.value.hours_to_craft + hours_remaining
        for item in starting_item.items_in_same_categories:
            if total_hours > 24:
                agendas.append(Agenda())
            else:
                for agenda in cls.get_all_agendas_for_item(item, total_hours):
                    if not agenda and not final_item and 20 < total_hours <= 24:
                        agenda.add(starting_item)
                        agendas.append(agenda)
                        final_item = True
                    elif agenda:
                        agenda.add(starting_item)
                        agendas.append(agenda)
        return agendas

    @classmethod
    def get_all_agendas(cls):
        out: Sequence[Agenda] = []
        for item in WorkshopItem:
            out.extend(cls.get_all_agendas_for_item(item))
        return out

    def __init__(self):
        self.items: Deque[WorkshopItem] = deque(maxlen=6)

    def __iter__(self):
        return (item for item in self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return " -> ".join(str(item) for item in self)

    @property
    def total_cowries(self) -> int:
        return sum(
            item.value.value * 2 if i != 0 else item.value.value
            for i, item in enumerate(self)
        )

    @property
    def total_hours(self) -> int:
        return sum(item.value.hours_to_craft for item in self)

    @property
    def cowries_per_hours(self) -> int:
        if self.total_hours == 0:
            return 0
        return self.total_cowries // self.total_hours

    def add(self, item: WorkshopItem) -> None:
        self.items.appendleft(item)
