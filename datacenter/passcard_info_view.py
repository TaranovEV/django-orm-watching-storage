from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration, get_duration, is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        one_visits = {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(one_visits)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
