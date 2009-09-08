from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

from dances.models import Dance

@login_required
def your_dances(request, template_name="dance/your_dances.html"):
    return render_to_response(template_name, {
        "groups": Dance.objects.filter(members=request.user).order_by("name"),
    }, context_instance=RequestContext(request))
    
def dances(request, template_name="dance/dances.html"):
    
    groups = BasicGroup.objects.filter()
    
    return render_to_response(template_name, {
        'dances': dances,
    }, context_instance=RequestContext(request))    