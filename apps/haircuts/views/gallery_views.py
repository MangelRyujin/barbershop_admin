from django.shortcuts import render
from apps.accounts.decorators import group_required
from apps.haircuts.filters import HairCutFilter
from apps.haircuts.forms import HairCutForm,GalleryForm
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging
from apps.haircuts.models import Gallery, HairCut
from utils.pagination import pagination
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required
import base64
from django.core.files.base import ContentFile

# haircut view (index)
@group_required('administrador')
@staff_member_required(login_url='/')
def gallery(request):
    context=_show_gallery(request)
    context["create_form"]=GalleryForm()
    return render(request,'gallery_templates/index.html',context)

# Charge result table
@staff_member_required(login_url='/')
def gallery_table_results(request):
    context=_show_gallery(request)
    return  render(request,'gallery_templates/table_results.html',context)
    
# filter haircuts
def _show_gallery(request):
    gallery = Gallery.objects.all()
    return pagination(request,gallery)

# haircut create form
@staff_member_required(login_url='/')
def gallery_create(request):
    context={}
    if request.method == "POST":
        form = GalleryForm()
        cropped_image_data = request.POST.get('cropped_image', '')
        if cropped_image_data:
            # Extraer la parte base64 de los datos
            format, imgstr = cropped_image_data.split(';base64,') 
            ext = format.split('/')[-1]  # Obtener la extensión (jpeg, png)
            
            # Decodificar la imagen
            data = ContentFile(base64.b64decode(imgstr), name=f'cropped_image.{ext}')
            # Crear tu modelo con la imagen recortada
            # Ejemplo:
            gallery_item = Gallery(image=data)
            gallery_item.name = gallery_item.image.name
            gallery_item.save()
        
            context['message']='Creado correctamente'
        else:
            context['error']='Corrige los errores'
        context['create_form']=form
        return render(request,'gallery_templates/actions/galleryCreate/galleryCreateForm.html',context) 
    form = GalleryForm()
    context['create_form']=form
    return render(request,'gallery_templates/actions/galleryCreate/galleryCreateForm.html',context) 



# Delete result table
@staff_member_required(login_url='/')
def gallery_delete(request,pk):
    picture = Gallery.objects.filter(pk=pk).first()
    context={"picture":picture}
    if request.method == "POST":
        if picture:
            picture.delete()
            context["picture"]=None
            context['message']=f'Imagen eliminada'
    return render(request,'gallery_templates/picture.html',context)
    
