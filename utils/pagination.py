from django.shortcuts import render
from apps.accounts.decorators import group_required
from apps.haircuts.filters import HairCutFilter
from apps.haircuts.forms import HairCutForm
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging
from apps.haircuts.models import HairCut
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required


# Pagination
def pagination(request,filter_list):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    paginator = Paginator(filter_list, 100)  
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context