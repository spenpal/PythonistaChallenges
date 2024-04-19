# April Monthly Challenge

_Date sorting_

Your task this month is to sort a set of dates based on a set of operations. You will receive a list of dates in the format `DD-MM-YYYY_HH:MM`, like this: `10-02-2018_12:30`.
Using that list, you must sort the dates based on another argument, which will contain a list of operations you must apply to the list (they must be applied in the order provided by the list).

Here is a list of possible operations:

-   `ASC` or `DSC` - sort the dates in ascending or descending order, respectively. These are mutually exclusive (only one will be present).
    Note that ascending would mean the oldest date is first, while descending would mean the newest date is first.
-   `UP-(MM)` - Any date with a month of MM should be pushed up the list by one
-   `DOWN-(DD)` - Any date with a day of DD should be pushed down the list by one
-   `TOP-(YYYY)` - Any date with a year of YYYY should be sent to the top of the list
-   `BOT-(YYYY)` - Any date with a year of YYYY should be sent to the bottom of the list

Each operation may only be applied to a date **once**.

An example is available on mystbin: https://mystb.in/WarrenRyanUniversity

Your code should contain a `sort_dates` function that takes 2 arguments, the list of dates and the list of operations, and returns the sorted list of dates.

```python
def sort_dates(dates: list[str], operations: list[str]) -> list[str]:
    ...
```

Your test cases:
Once again they were too long, so please view them on mystbin: https://mystb.in/WarrenRyanUniversity

Bonus Challenges:

1. Do not use any date libraries
