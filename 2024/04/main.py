from typing import NamedTuple


class Date(NamedTuple):
    day: str
    month: str
    year: str
    hour: str
    minute: str

    def __lt__(self, other: "Date") -> bool:
        return (self.year, self.month, self.day, self.hour, self.minute) < (
            other.year,
            other.month,
            other.day,
            other.hour,
            other.minute,
        )

    def __str__(self) -> str:
        return f"{self.day}-{self.month}-{self.year}_{self.hour}:{self.minute}"


def sort_dates(dates: list[str], operations: list[str]) -> list[str]:
    dates = [
        Date(date[:2], date[3:5], date[6:10], date[11:13], date[14:]) for date in dates
    ]

    length = len(dates)
    for operation in operations:
        op = operation.split("-")
        match op[0]:
            case "ASC":
                dates.sort()
            case "DSC":
                dates.sort(reverse=True)
            case "UP":
                month = op[1]
                for i in range(1, length):
                    if dates[i].month == month:
                        dates[i - 1], dates[i] = dates[i], dates[i - 1]
            case "DOWN":
                day = op[1]
                i = 0
                while i < length - 1:
                    if dates[i].day == day:
                        if dates[i + 1].day != day:
                            dates[i], dates[i + 1] = dates[i + 1], dates[i]
                        i += 1
                    i += 1
            case "TOP":
                year = op[1]
                for i in range(length):
                    if dates[i].year == year:
                        dates.insert(0, dates.pop(i))
            case "BOT":
                year = op[1]
                i, last_index = 0, length - 1
                while i <= last_index:
                    if dates[i].year == year:
                        dates.append(dates.pop(i))
                        last_index -= 1
                    else:
                        i += 1

    return [str(date) for date in dates]
