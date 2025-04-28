from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from account.decorators import check_authoritation
from pagadurias.models import Pagaduria
from django.db.models import Sum
from django.contrib import messages

@login_required
@check_authoritation
def lista_operaciones(request):
    # Mostrar solo las pagadurías aprobadas en Comercial, Financiero, Riesgos y que aún no estén aprobadas en Operaciones
    pagadurias = Pagaduria.objects.filter(
        estadoComercial='Aprobado',
        estadoFinanciero='Aprobado',
        estadoRiesgos='Aprobado',
        estadoOperaciones=False  # Aún no aprobadas por operaciones
    )
    return render(request, 'operaciones/lista_operaciones.html', {'pagadurias': pagadurias})

@login_required
@check_authoritation
def aprobar_operaciones(request, nombre, tokenControl):
    pagaduria = get_object_or_404(Pagaduria, nombre=nombre, tokenControl=tokenControl)
    
    # Obtener todas las sucursales relacionadas
    sucursales = pagaduria.sucursales.all()
    
    # Calcular totales
    totales = sucursales.aggregate(
        totalEmpleados=Sum('totalEmpleados'),
        indefinidos=Sum('empleadosIndefinidos'),
        fijos=Sum('empleadosFijo'),
        obra=Sum('empleadosObraLabor'),
        otros=Sum('empleadosOtros'),
        salario1y2=Sum('empleadosSalario1y2'),
        salario2y4=Sum('empleadosSalario2y4'),
        salarioMax4=Sum('empleadosSalariomax4')
    )
    
    if request.method == 'POST':
        # Aquí sí aprobarías, cuando envíen el formulario
        pagaduria.estadoOperaciones = True
        pagaduria.save()
        messages.success(request, "Pagaduría aprobada en operaciones correctamente.")
        return redirect('lista_operaciones')
    
    return render(request, 'operaciones/aprobar_operaciones.html', {
        'pagaduria': pagaduria,
        'sucursales': sucursales,
        'totales': totales
    })
