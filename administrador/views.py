from django.contrib.auth.decorators import login_required
from account.decorators import check_authoritation, check_superuser
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from pagadurias.models import Pagaduria
from account.forms import UpdateUser
from django.http import JsonResponse
from django.contrib import messages
from account.models import User
from django.db.models import Q
import requests
from account.utils import NotificacionUsuarioService


def administrador(request):
    if not request.user.is_authenticated:
        return redirect('login')  # O la vista adecuada para usuarios anónimos

    if not request.user.checkForTI:
        return redirect('waiting_for_auth')

    return render(request, 'base.html')


@login_required
def callAndUpdatePagaduriasExistLinix(request):
    url = 'http://127.0.0.1:8080/api-coovitel/pagadurias'
    headers = {
        'Authorization': 'Token aec701eea92de00363e5c40dbdcad62ee7c3eb99'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for regisPagaduria in data['data']:
            checkPagaduria = Pagaduria.objects.filter(nombre=regisPagaduria['n_nomina'])
            if not checkPagaduria.exists():
                createdPagaduria = Pagaduria.objects.create(
                    nombre=regisPagaduria['n_nomina'],
                    nit=regisPagaduria['nit'],
                    razonSocial=regisPagaduria['n_razon'],
                    sigla=regisPagaduria['sigla'],
                    tipoEmpresa=regisPagaduria['k_tipoem'],
                    departamento=regisPagaduria['departamento'],
                    ciudad=regisPagaduria['ciudad'],
                    numeroCedulaRepresentante=regisPagaduria['num_representante'],
                    nombreRepresentante=regisPagaduria['representante'],
                    estado="Aprobado",
                    estadoFinanciero="Aprobado",
                    estadoRiesgos="Aprobado",
                    estadoComercial="Aprobado",
                    estadoOperaciones=True
                )
                createdPagaduria.save()
        return JsonResponse({'success': True, 'message': 'Pagadurias creadas correctamente', 'data': data}, status=200)
    else:
        return JsonResponse({'success': False, 'message': 'Error en la solicitud', 'status_code': response.status_code}, status=response.status_code)

@login_required
def usuarios(request):

    query = request.GET.get('nameUser', '')
    asesores = User.objects.all()
    if query:
        asesores = asesores.filter(
            Q(username__icontains=query) | Q(area__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    
    paginator = Paginator(asesores, 7)  # 10 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    user = None
    find = False
    formUser = None
    
    if request.method == "POST":
        form_type = request.POST.get('form-type')
        
        if form_type == 'open-user':
            userId = request.POST.get('user-id')
            user = User.objects.get(id=userId)
            find = True
            formUser = UpdateUser(instance=user)
        
        elif form_type == "update-user":
            userId = request.POST.get('user-id')
            if userId:
                user = User.objects.get(id=userId)
                formUser = UpdateUser(request.POST, instance=user)

                if formUser.is_valid():
                    formUser.save()
                    user.refresh_from_db()  # <-- Asegura que tienes el valor más actualizado

                    # ✅ Siempre que esté autorizado, envía el correo
                    if user.checkForTI:
                        try:
                            NotificacionUsuarioService.notificar_autorizacion(user)
                            messages.success(request, "Se ha enviado la notificación al usuario autorizado.")
                        except Exception as e:
                            messages.error(request, f"Error al enviar la notificación: {e}")

                    messages.success(request, "Se ha actualizado el Usuario con éxito")
                    return redirect('asesores')
                find = True
            
    return render(request, 'usuarios/usuarios.html', {
        'asesores': page_obj,
        'query': query,
        'paginator': paginator,
        'page_obj': page_obj,
        'user': user,
        'formUser': formUser,
        'find': find
    }) 