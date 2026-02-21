#!/usr/bin/env python3

"""datetime_tolerant: a time-zone tolerant datetime.

   Copyright 2026 by Akkana Peck:Share and enjoy under the GPL v2 or later.
"""

from datetime import datetime


class datetime_tolerant(datetime):
    default_tz = datetime.now().astimezone().tzinfo

    @classmethod
    def set_default_timezone(self, tz):
        if tz:
            __class__.default_tz = tz
        else:
            __class__.default_tz = datetime.now().astimezone().tzinfo
        print("Set default tz to", __class__.default_tz)

    def get_with_tz(self, t):
        if t.tzinfo:
            return t
        print("For", t, "applying default timezone", __class__.default_tz)
        return t.replace(tzinfo=__class__.default_tz)

    def __lt__(self, other):
        """A < operator for datetime that is tolerant of comparing
           timezone aware and unaware objects
        """
        return datetime.__lt__(self.get_with_tz(self), self.get_with_tz(other))

    def __gt__(self, other):
        return datetime.__gt__(self.get_with_tz(self), self.get_with_tz(other))

    def __eq__(self, other):
        return datetime.__eq__(self.get_with_tz(self), self.get_with_tz(other))

    def __sub__(self, other):
        print("Calculating", self, "-", other)
        print("Really calculating", self.get_with_tz(self),
              "-", self.get_with_tz(other))
        return datetime.__sub__(self.get_with_tz(self), self.get_with_tz(other))


if __name__ == '__main__':
    pass

