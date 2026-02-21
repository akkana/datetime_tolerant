#!/usr/bin/env python3

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from datetime_tolerant import datetime_tolerant

from datetime import timezone, timedelta


def test_datetime_tolerant():
    morning = datetime_tolerant(2026, 1, 1, 8, 0, 0)
    afternoon = datetime_tolerant(2026, 1, 1, 15, 0, 0)
    weeklater = datetime_tolerant(2026, 1, 8, 8, 0, 0)

    localtz = datetime_tolerant.now().astimezone().tzinfo
    morning_local = datetime_tolerant(2026, 1, 1, 8, 0, 0, tzinfo=localtz)
    afternoon_local = datetime_tolerant(2026, 1, 1, 15, 0, 0, tzinfo=localtz)
    weeklater_local = datetime_tolerant(2026, 1, 8, 8, 0, 0, tzinfo=localtz)

    morning_UTC = datetime_tolerant(2026, 1, 1, 8, 0, 0, tzinfo=timezone.utc)
    afternoon_UTC = datetime_tolerant(2026, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
    weeklater_UTC = datetime_tolerant(2026, 1, 8, 8, 0, 0, tzinfo=timezone.utc)

    assert morning < afternoon
    assert afternoon > morning
    assert morning < weeklater
    assert weeklater > afternoon
    assert morning_local != morning_UTC
    assert morning_local < morning_UTC or morning_local > morning_UTC
    assert afternoon - morning == timedelta(hours=7)
    assert weeklater - morning == timedelta(days=7)
    assert afternoon - morning == timedelta(hours=7)
    assert weeklater - morning == timedelta(days=7)

    # The default default is local
    assert morning == morning_local
    assert morning < afternoon_local
    assert morning_local < afternoon_local
    assert weeklater > afternoon_local
    assert afternoon - morning_local == timedelta(hours=7)
    assert weeklater - morning_local == timedelta(days=7)
    assert afternoon_local - morning == timedelta(hours=7)
    assert weeklater_local - morning == timedelta(days=7)

    # Explicitly default to local
    datetime_tolerant.set_default_timezone(localtz)
    assert morning == morning_local
    assert morning < afternoon_local
    assert morning_local < afternoon_local
    assert weeklater > afternoon_local
    assert afternoon - morning_local == timedelta(hours=7)
    assert weeklater - morning_local == timedelta(days=7)
    assert afternoon_local - morning == timedelta(hours=7)
    assert weeklater_local - morning == timedelta(days=7)

    # Default to UTC
    datetime_tolerant.set_default_timezone(timezone.utc)
    print("morning_UTC:", morning_UTC)
    assert morning == morning_UTC
    assert morning < afternoon_UTC
    assert weeklater > afternoon_UTC
    assert afternoon - morning_UTC == timedelta(hours=7)
    assert weeklater - morning_UTC == timedelta(days=7)
    assert afternoon_UTC - morning == timedelta(hours=7)
    assert weeklater_UTC - morning == timedelta(days=7)
    assert afternoon - morning_UTC == timedelta(hours=7)
    assert weeklater - morning_UTC == timedelta(days=7)
