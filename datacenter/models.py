from django.db import models
from django.utils.timezone import localtime
import datetime


def get_duration(visit):
    end_time = visit.leaved_at
    if visit.leaved_at is None:
        end_time = localtime()
    return (end_time - visit.entered_at).total_seconds()


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    return '{}ч {}мин'.format(hours, minutes)


def is_visit_long(visit, minutes=60):
    duration_seconds = get_duration(visit)
    duration_minutes = duration_seconds / 60
    return duration_minutes > minutes


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )
