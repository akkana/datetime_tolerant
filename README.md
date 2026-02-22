# Time Zone Tolerant Datetime

**datetime_tolerant** is a class derived from datetime that's more tolerant
in comparisons like <, > and == and in date subtraction.

datetime_tolerant objects that have timezones specified ("timezone aware")
will honor their time zones.
If a datetime_tolerant object doesn't have a timezone specified
(i.e. it's "unaware" or "naive"),
by default, it will compare as if it's in the local time zone.
However, you can change that default to a specific timezone
with `set_default_timezone`:

```
datetime_tolerant.set_default_timezone(timezone.utc)
```

Aside from that, datetime_tolerant should behave exactly like a regular
datetime and can be used anywhere you'd use a regular datetime.

### Why?

Python's datetime class drives me crazy.

Any given datetime object might or might not have a timezone.
Any given function might or might not return a timezone-aware datetime.
If you ever mess up and call a function that returns a timezone when you
didn't expect one, or vice versa, or if a function you call changes in
that respect, now you have a hidden time bomb that will crash your
program the next time you do any sort of comparison with or
subtraction from another datetime, and by then, you may have no idea
way of finding out where the problematic time came from so you can
guard against it happening again.

*datetime_tolerant* unfortunately doesn't fully fix that problem, because
there are so many other functions that return a standard datetime.
For instance, flask and squalchemy store timezone-aware datetimes
in the database (at least if you're using postgresql),
but they don't offer any control over what timezone is used.
So it's still necessary to put in a lot of checks;
but I'm hoping if I get into the habit of converting every *datetime*
to a *datetime_tolerant* before doing anything else with it, maybe that
will at least help.
