from django.shortcuts import render
from apps.accounts.decorators import group_required
from apps.haircuts.filters import HairCutFilter
from apps.haircuts.forms import HairCutForm
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging
from apps.haircuts.models import HairCut
from utils.pagination import pagination
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required

# haircut view (index)
@group_required('administrador')
@staff_member_required(login_url='/')
def haircut(request):
    context=_show_haircut(request)
    context["create_form"]=HairCutForm()
    return render(request,'haircuts_templates/index.html',context)

# Charge result table
@staff_member_required(login_url='/')
def haircut_table_results(request):
    context=_show_haircut(request)
    return  render(request,'haircuts_templates/table_results.html',context)
    
# filter haircuts
def _show_haircut(request):
    haircuts = HairCutFilter(request.GET, queryset=HairCut.objects.all())
    return pagination(request,haircuts.qs)

# haircut create form
@staff_member_required(login_url='/')
def haircut_create(request):
    context={}
    if request.method == "POST":
        form = HairCutForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
            form = HairCutForm()
            context['message']='Creado correctamente'
        else:
            context['error']='Corrige los errores'
        context['create_form']=form
        return render(request,'haircuts_templates/actions/haircutCreate/haircutCreateForm.html',context) 
    form = HairCutForm()
    context['create_form']=form
    return render(request,'haircuts_templates/actions/haircutCreate/haircutCreateForm.html',context) 


# haircut update forms
@staff_member_required(login_url='/')
def haircut_update(request,pk):
    haircut = HairCut.objects.filter(pk=pk).first()
    form = HairCutForm(instance=haircut)
    context={}
    context['haircut']=haircut
    context['form']=form
    return render(request,'haircuts_templates/actions/haircutUpdate/haircutUpdateForm.html',context) 

# haircut main information update form
@staff_member_required(login_url='/')
def haircut_form_update(request,pk):
    context={}
    if request.method == "POST":
        haircut = HairCut.objects.filter(pk=pk).first()
        form = HairCutForm(request.POST,request.FILES,instance=haircut)
        if form.is_valid():
            haircut_form_valid=form.save(commit=False)
            haircut_form_valid._change_reason = f'Categoría {haircut.name} modificada'
            haircut_form_valid.save()
            message="Editado correctamente"
            context['message']=message
        else:
            message="Corrige los errores"
            context['error']=message
        context['haircut']=haircut
        context['form']=form
        return render(request,'haircuts_templates/actions/haircutUpdate/haircutUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def haircut_delete(request,pk):
    haircut = HairCut.objects.filter(pk=pk).first()
    context={"haircut":haircut}
    if request.method == "POST":
        if haircut:
            haircut_name=haircut.name
            haircut.delete()
            context["haircut"]=[]
            context['message']=f'El corte ha sido eliminado'
    return render(request,'haircuts_templates/haircut.html',context)
    


# Detail user haircut table
@staff_member_required(login_url='/')
def haircut_detail(request,pk):
    haircut = HairCut.objects.filter(pk=pk).first()
    return  render(request,'haircuts_templates/actions/haircutDetail/haircutDetail.html',{"haircut":haircut})
     