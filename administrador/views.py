from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
from pagadurias.models import Pagaduria

def administrador(request):
    return render(request, 'base.html')

def callAndUpdatePagaduriasExistLinix(request):
    url = 'http://127.0.0.1:8001/api-coovitel/pagadurias'
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
                )
                createdPagaduria.save()
        return JsonResponse({'success': True, 'message': 'Pagadurias creadas correctamente', 'data': data}, status=200)
    else:
        return JsonResponse({'success': False, 'message': 'Error en la solicitud', 'status_code': response.status_code}, status=response.status_code)
