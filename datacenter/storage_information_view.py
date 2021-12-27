from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration,get_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    filtered_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit in filtered_visits:
        one_person = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit),
        }
        non_closed_visits.append(one_person)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
