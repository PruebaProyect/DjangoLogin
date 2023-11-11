from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import openai  # pip install openai
from rich import print  # pip install rich
from . models import Question,Activity1,Activity3,ActivityN
# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    # Obtener el nombre de usuario de la sesión
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'home'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        context = {'username': username}
        return render(request, 'home.html', context)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")
    

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Las contraseñas no coinciden!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            request.session['username'] = username
            return redirect('home')
        else:
            return HttpResponse ("Usuario y Contraseña incorrectos!!!")
    return render (request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def __prompt(request) -> str:
    opcion_seleccionada = request.POST.get('opcion_seleccionada')
    prompt = opcion_seleccionada
    return prompt


def procesar_seleccion(request):
    max_interacciones = 1  # Establece el número máximo de interacciones deseado
    interacciones = 0   
    responses = []
    if request.method == 'POST':
        opcion_seleccionada = request.POST.get('opcion_seleccionada')
        openai.api_key = "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"
        # Contexto del asistente
        context = {"role": "system",
                "content": "Eres un Profesional que asistira para la prevencion de fatiga laboral en el personal medico de una clinica."}
        messages = [context]
        while  interacciones < max_interacciones:
            content = __prompt(request)
            messages.append({"role": "user", "content": content})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            response_content = response.choices[0].message.content
            messages.append({"role": "assistant", "content": response_content})
            print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
            response_content = response_content.replace("\n", "<br>")
            formatted_text = f"{response_content}"
            responses.append(formatted_text)
            interacciones += 1
    return render(request, 'actividad5.html', {'resultado': responses})


def actividad1(request):
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'otra_pagina'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        contexto = {
            'titulo': 'Actividad 1 - Programación de Turnos Optimizada',
            'contenido': 'Contenido de la Actividad 1',
            'username': username,
        }
        return render(request, 'actividad1.html', contexto)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")


def actividad2(request):
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'otra_pagina'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        contexto = {
            'titulo': 'Actividad 2 - Recordatorio de Descansos Regulares',
            'contenido': 'Contenido de la Actividad 2',
            'username': username,
        }
        return render(request, 'actividad2.html', contexto)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")


def actividad3(request):
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'otra_pagina'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        contexto = {
            'titulo': 'Actividad 3 - Registro de Jornada Laboral',
            'contenido': 'Contenido de la Actividad 3',
            'username': username,
        }
        return render(request, 'actividad3.html', contexto)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")


def actividad4(request):
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'otra_pagina'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        contexto = {
            'titulo': 'Actividad 4 - Ejercicios de Respiración y Relajación',
            'contenido': 'Contenido de la Actividad 4',
            'username': username,
        }
        return render(request, 'actividad4.html', contexto)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")


def actividad5(request):
    datos = Question.objects.all()
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'otra_pagina'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        contexto = {
            'titulo': 'Actividad 5 - Registro de Síntomas de Fatiga',
            'contenido': 'Contenido de la Actividad 5',
            'username': username,
            'preguntas' : datos,
        }
        return render(request, 'actividad1.html', contexto)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")


def actividad6(request):
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'otra_pagina'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        contexto = {
            'titulo': 'Actividad 6 - Sugerencias para una Alimentación Saludable',
            'contenido': 'Contenido de la Actividad 6',
            'username': username,
        }
        return render(request, 'actividad6.html', contexto)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")


def actividad7(request):
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'otra_pagina'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        contexto = {
            'titulo': 'Actividad 7 - Planificación de Actividades Fuera del Trabajo',
            'contenido': 'Contenido de la Actividad 7',
            'username': username,
        }
        return render(request, 'actividad7.html', contexto)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")


def actividad8(request):
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'otra_pagina'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        contexto = {
            'titulo': 'Actividad 8 - Recordatorios de Hidratación',
            'contenido': 'Contenido de la Actividad 8',
            'username': username,
        }
        return render(request, 'actividad8.html', contexto)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")


def actividad9(request):
    username = request.session.get('username', None)
    if username:
        # Hacer algo con el nombre de usuario en la vista 'otra_pagina'
        # Por ejemplo, pasarlo al contexto para mostrarlo en la plantilla
        contexto = {
            'titulo': 'Actividad 9 - Capacitación y Actualización Continua',
            'contenido': 'Contenido de la Actividad 9',
            'username': username,
        }
        return render(request, 'actividad9.html', contexto)
    else:
        # Manejar el caso en el que el nombre de usuario no está en la sesión
        return HttpResponse("Debe iniciar sesión primero.")


from django.shortcuts import render


def vistaactividad1(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        horas_diarias = request.POST['horas_diarias']
        horas_descanso = request.POST['horas_descanso']
        periodos_comidas = request.POST['periodos_comidas']
        trabajo_sabados = request.POST['trabajo_sabados']
        trabajo_domingos = request.POST['trabajo_domingos']
        # Combina los datos en un solo texto
        resultado = f"Actualmente trabajo {horas_diarias} horas diarias con {horas_descanso} horas de descanso y {periodos_comidas} periodos para comidas, además {trabajo_sabados} trabajo sábados y {trabajo_domingos} domingos."
        max_interacciones = 1  # Establece el número máximo de interacciones deseado
        interacciones = 0   
        responses = []
        nuevo_reg=Activity1(act1_usuario = username, horas_diarias = horas_diarias, horas_descanso=horas_descanso, periodos_descando=periodos_comidas,trabajo_sabado = trabajo_sabados, trabajo_domingo=trabajo_domingos)
        nuevo_reg.save()
        if request.method == 'POST':
            openai.api_key = "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"
            # Contexto del asistente
            context = {"role": "system",
                    "content": "Eres un Profesional que asistira para la prevencion de fatiga laboral analizando la carga laboral del trabajador con periodos de descanso incluidos fines de semana."}
            messages = [context]
            while  interacciones < max_interacciones:
                messages.append({"role": "user", "content": resultado})
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                response_content = response.choices[0].message.content
                messages.append({"role": "assistant", "content": response_content})
                print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
                response_content = response_content.replace("\n", "<br>")
                formatted_text = f"{response_content}"
                responses.append(formatted_text)
                interacciones += 1
            return render(request, 'actividad1.html', {'resultado': responses})
    return render(request, 'actividad1.html')


def vistaactividad3(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        turno = request.POST['trabajo_turno']
        hora_inicio = request.POST['hora_inicio']
        hora_fin = request.POST['hora_fin']
        actividad_relevante = request.POST['actividad_relevante']
        nota_adicional = request.POST['nota_adicional']
        inicio_trabajo = request.POST['inicio_trabajo']
        final_trabajo = request.POST['final_trabajo']
        # Combina los datos en una cadena
        resultado = f"Hoy tuve el turno de la {turno}. La hora de Inicio fue a las {hora_inicio} de la {inicio_trabajo} y la hora de Fin de turno fue a las {hora_fin} de la {final_trabajo}. En el turno tuve actividades extras o relevantes como {actividad_relevante}. Además tengo una nota adicional al respecto de este turno que indica que {nota_adicional}. ¿Verificar si estas circunstancias de carga laboral puede generar fatiga?"
        max_interacciones = 1  # Establece el número máximo de interacciones deseado
        interacciones = 0   
        responses = []
        nuevo_reg=Activity3(act1_usuario = username, turno = turno, turno_inicio=hora_inicio, 
                            turno_inicio_periodo=inicio_trabajo,turno_final = hora_fin, turno_final_periodo=final_trabajo,
                            turno_actividades=actividad_relevante,turno_notas=nota_adicional)
        nuevo_reg.save()
        if request.method == 'POST':
            openai.api_key = "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"
            # Contexto del asistente
            context = {"role": "system",
                    "content": "Eres un Profesional que asistira para la prevencion de fatiga laboral en el personal medico analizando la carga horaria de trabajo asi como actividades relevantes y notas adicionales dentro de su turno."}
            messages = [context]
            while  interacciones < max_interacciones:
                messages.append({"role": "user", "content": resultado})
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                response_content = response.choices[0].message.content
                messages.append({"role": "assistant", "content": response_content})
                print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
                response_content = response_content.replace("\n", "<br>")
                formatted_text = f"{response_content}"
                responses.append(formatted_text)
                interacciones += 1
            return render(request, 'actividad3.html', {'resultado': responses})

    return render(request, 'actividad3.html')


def vistaactividad1(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        horas_diarias = request.POST['horas_diarias']
        horas_descanso = request.POST['horas_descanso']
        periodos_comidas = request.POST['periodos_comidas']
        trabajo_sabados = request.POST['trabajo_sabados']
        trabajo_domingos = request.POST['trabajo_domingos']
        # Combina los datos en un solo texto
        resultado = f"Actualmente trabajo {horas_diarias} horas diarias con {horas_descanso} horas de descanso y {periodos_comidas} periodos para comidas, además {trabajo_sabados} trabajo sábados y {trabajo_domingos} domingos."
        max_interacciones = 1  # Establece el número máximo de interacciones deseado
        interacciones = 0   
        responses = []
        nuevo_reg=Activity1(act1_usuario = username, horas_diarias = horas_diarias, horas_descanso=horas_descanso, periodos_descando=periodos_comidas,trabajo_sabado = trabajo_sabados, trabajo_domingo=trabajo_domingos)
        nuevo_reg.save()
        if request.method == 'POST':
            openai.api_key = "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"
            # Contexto del asistente
            context = {"role": "system",
                    "content": "Eres un Profesional que asistira para la prevencion de fatiga laboral analizando la carga laboral del trabajador con periodos de descanso incluidos fines de semana."}
            messages = [context]
            while  interacciones < max_interacciones:
                messages.append({"role": "user", "content": resultado})
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                response_content = response.choices[0].message.content
                messages.append({"role": "assistant", "content": response_content})
                print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
                response_content = response_content.replace("\n", "<br>")
                formatted_text = f"{response_content}"
                responses.append(formatted_text)
                interacciones += 1
            return render(request, 'actividad1.html', {'resultado': responses})
    return render(request, 'actividad1.html')


def vistaactividad6(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        # Combina los datos en una cadena
        resultado = f"Necesito lista de 10 practicas para mejorar la alimentacion para evitar la fatiga laboral."
        max_interacciones = 1  # Establece el número máximo de interacciones deseado
        interacciones = 0   
        responses = []
        nuevo_reg=ActivityN(actN_usuario = username, actividad = 'OK Actividad 6')
        nuevo_reg.save()
        if request.method == 'POST':
            openai.api_key = "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"
            # Contexto del asistente
            context = {"role": "system",
                    "content": "Eres un Profesional que asistira para la prevencion de fatiga laboral en el personal medico de una clinica."}
            messages = [context]
            while  interacciones < max_interacciones:
                messages.append({"role": "user", "content": resultado})
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                response_content = response.choices[0].message.content
                messages.append({"role": "assistant", "content": response_content})
                print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
                response_content = response_content.replace("\n", "<br>")
                formatted_text = f"{response_content}"
                responses.append(formatted_text)
                interacciones += 1
            return render(request, 'actividad6.html', {'resultado': responses})
    return render(request, 'actividad6.html')


def vistaactividad7(request):
    if request.method == 'POST':
        username = request.session.get('username', None)
        # Combina los datos en una cadena
        resultado = f"Necesito lista de 10 actividades relajantes para realizar despues del trabajo en un turno de clinica."
        max_interacciones = 1  # Establece el número máximo de interacciones deseado
        interacciones = 0   
        responses = []
        nuevo_reg=ActivityN(actN_usuario = username, actividad = 'OK Actividad 7')
        nuevo_reg.save()
        if request.method == 'POST':
            openai.api_key = "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"
            # Contexto del asistente
            context = {"role": "system",
                    "content": "Eres un Profesional que asistira para la prevencion de fatiga laboral en el personal medico de una clinica."}
            messages = [context]
            while  interacciones < max_interacciones:
                messages.append({"role": "user", "content": resultado})
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                response_content = response.choices[0].message.content
                messages.append({"role": "assistant", "content": response_content})
                print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
                response_content = response_content.replace("\n", "<br>")
                formatted_text = f"{response_content}"
                responses.append(formatted_text)
                interacciones += 1
            return render(request, 'actividad7.html', {'resultado': responses})
    return render(request, 'actividad7.html')
