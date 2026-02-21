## Time Zone Tolerant Datetime

Python's datetime class drives me crazy.

Any given datetime object might or might not have a timezone. Any
given function might or might not return a timezone-aware datetime. If
you ever mess up and call a function that returns a timezone when you
didn't expect one, or vice versa, or a function you call changes in
that respect, now you have a hidden time bomb that will crash your
program the next time you do a comparison with or subtraction from
another datetime.

**datetime_tolerant** is a class derived from datetime that's more tolerant
in comparisons like <, > and == and in date subtraction.

By default, if a datetime_tolerant doesn't have a timezone specified,
it will compare as if it's in the local time zone.
However, you can make it default to a specific other timezone
with `set_default_timezone`:

```
datetime_tolerant.set_default_timezone(timezone.utc)
```

Aside from that, datetime_tolerant should behave exactly like a regular
datetime and can be used anywhere you'd use a regular datetime.
