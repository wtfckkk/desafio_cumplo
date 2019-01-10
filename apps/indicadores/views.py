from django.shortcuts import render
from apps.indicadores.forms import ConsultaForm
from apps.indicadores.services import get_dolares_entre_fechas, get_uf_entre_fechas, get_tmc_entre_fechas, getDatesTmc, getTiposTmc

def welcome(request):
    return render(request, 'indicadores/welcome.html')

def index(request):

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():

            # Save form (model=consulta)
            form.save()

            # Get forms values
            start = form.cleaned_data['fecha_inicio']
            end = form.cleaned_data['fecha_fin']
            tipo = form.cleaned_data['tipo_consulta']

            # Validate coherence between input dates #
            if start >= end:
                return render(request, 'indicadores/indicadores_form.html', {'form': form,'error':'La fecha de inicio debe ser menor a la final'})

            # Validate if Type=Dolar , consume API and return
            if str(tipo) == 'Dólar':
                dolar = get_dolares_entre_fechas(start.year, start.month, start.day, end.year, end.month, end.day)
                return render( request, 'indicadores/dolar_uf_list.html', {
                    'indicadores': dolar,
                    'flag':str(tipo),
                    'start': start,
                    'end': end}
                )

            # Validate if Type=UF , consume API and return
            if str(tipo) == 'UF':
                uf = get_uf_entre_fechas(start.year, start.month, start.day, end.year, end.month, end.day)
                return render(request, 'indicadores/dolar_uf_list.html', {
                    'indicadores': uf,
                    'flag':str(tipo),
                    'start': start,
                    'end': end}
                )

            # Validate if Type=TMC , consume API, think and return
            if str(tipo) == 'TMC':
                tmc = get_tmc_entre_fechas(start.year, start.month, end.year, end.month)

                if 'valores' not in tmc:
                    return render(request, 'indicadores/tmc_list.html', {'indicadores': False})

                # Sort by (date|type)
                tmc['valores'] = sorted(sorted(tmc['valores'], key = lambda x : x['Tipo']), key = lambda x : x['Fecha'])

                # Get lists of types and dates
                list_tipos = getTiposTmc(tmc)
                list_dates = getDatesTmc(tmc)

                data = {}
                tmcs = tmc['valores']

                # Create series of Maximum by Type
                for idx, tipotmc in enumerate(list_tipos):
                    data[str(tipotmc)] = {}
                    data[str(tipotmc)]['name'] = 'Máximo del Tipo {}' .format(tipotmc)
                    data[str(tipotmc)]['tipo'] = tipotmc
                    largest_so_far = float(0)
                    j = 0
                    data[str(tipotmc)]['data'] = []
                    for k, v in enumerate(tmcs):
                        if v['Tipo'] == tipotmc:
                            data[str(tipotmc)]['data'].append('0')
                            if float(v['Valor']) > largest_so_far:
                                largest_so_far = float(v['Valor'])
                                largest_so_far_k = j
                            j = j + 1
                    data[str(tipotmc)]['data'][largest_so_far_k] = str(largest_so_far)
                maximum_series_data = data

                return render(request, 'indicadores/tmc_list.html', {
                    'indicadores': tmc,
                    'list_tipos':list_tipos,
                    'list_dates':list_dates,
                    'flag':str(tipo),
                    'start':start,
                    'end': end,
                    'maximum_series_data': maximum_series_data}
                )
        else:
            return render(request, 'indicadores/indicadores_form.html', {'form': form})
    else:
        form = ConsultaForm()
        return render(request, 'indicadores/indicadores_form.html', {'form':form})
