from typing import List

from agenda import Agenda

if __name__ == "__main__":
    most_cowries: List[Agenda] = []
    maximum = -1
    for agenda in Agenda.get_all_agendas():
        if agenda.total_cowries > maximum:
        # if agenda.total_cowries > maximum and len(agenda) == 6:
            maximum = agenda.total_cowries
            most_cowries.clear()
            most_cowries.append(agenda)
        elif agenda.total_cowries == maximum:
        # elif agenda.total_cowries == maximum and len(agenda) == 6:
            most_cowries.append(agenda)
    for agenda in most_cowries:
        print("\n".join(
            [
                f"Total Cowries: {agenda.total_cowries}",
                f"Total Hours: {agenda.total_hours}",
                f"Agenda: {str(agenda)}",
            ]
        ))    
