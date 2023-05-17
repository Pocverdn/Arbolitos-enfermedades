import pyttsx3
import webbrowser
import tkinter as tk

#----------------------------------------------Voz de Gio-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
#_------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, question, disease):
        self.question = question
        self.disease = disease
        self.yes = None
        self.no = None


def build_tree(question):
    root = Node(question[0], None)
    before_level = [root]
    for level in range(1, 6):
        current_level = []
        for node in before_level:
            node.yes = Node(question[level], None)
            node.no = Node(question[level], None)
            current_level.append(node.yes)
            current_level.append(node.no)
        before_level = current_level
    return root


def add_diseases(node, diseases, level):
    node_aux = node
    for i in range(7):
        if diseases[level][i] == "Si" and node_aux.yes is not None:
            node_aux = node_aux.yes
        elif diseases[level][i] == "Si" and node_aux.yes is None:
            node_aux.yes = Node(None, diseases[level][6])
        if diseases[level][i] == "No" and node_aux.no is not None:
            node_aux = node_aux.no
        elif diseases[level][i] == "No" and node_aux.no is None:
            node_aux.no = Node(None, diseases[level][6])


def travel(node, answers):
    node_aux = node
    for i in range(6):
        if not answers[i]:
            node_aux = node_aux.yes
        else:
            node_aux = node_aux.no

    print(f'Enfermedad: {node_aux.disease}')

    if node_aux.disease == "No tiene enfermedad":
        engine.say(f'Felicidades, por lo visto se encuentra sano')
        engine.say(f'¿Desea ver un gameplay de vegeta? oprime la letra s para si, de lo contrario oprime la letra n')
        engine.runAndWait()
        aux = input(f'¿Ver video? (S/N): ')
        if aux.lower() == "s":
            engine.say(
                f'Desde potoncio industries (patente en proceso), le damos las gracias por usar nuestro programa, en breve se reproducira su video, recuerde que el programa aun no se acaba, puede tomar el examen tantas veces usted quiera, solo oprima s para iniciar un nuevo diagnostico, de lo contrario oprima n')
            engine.runAndWait()
            webbrowser.open(videos[node_aux.disease])
        if aux.lower() == "n":
            engine.say(
                f'Desde potoncio industries (patente en proceso), le damos las gracias por usar nuestro programa, recuerde que el programa aun no se acaba, puede tomar el examen tantas veces usted quiera, solo oprima s para iniciar un nuevo diagnostico, de lo contrario oprima n')
            engine.runAndWait()

    else:
        engine.say(f'Lamento informarle que usted sufre de {node_aux.disease}')
        engine.say(
            f'¿Desea ver un video hablando sobre {node_aux.disease}? oprime la letra s para si, de lo contrario oprime la letra n')
        engine.runAndWait()
        aux = input(f'¿Ver video? (S/N): ')
        if aux.lower() == "s":
            engine.say(
                f'Desde potoncio industries (patente en proceso), le damos las gracias por usar nuestro programa, en breve se reproducira su video, recuerde que el programa aun no se acaba, puede tomar el examen tantas veces usted quiera, solo oprima s para iniciar un nuevo diagnostico, de lo contrario oprima n')
            engine.runAndWait()
            webbrowser.open(videos[node_aux.disease])
        if aux.lower() == "n":
            engine.say(f'Entendido, deseo lo mejor para su tratamiento')
            engine.say(
                f'Desde potoncio industries (patente en proceso), le damos las gracias por usar nuestro programa, recuerde que el programa aun no se acaba, puede tomar el examen tantas veces usted quiera, solo oprima s para iniciar un nuevo diagnostico, de lo contrario oprima n')
            engine.runAndWait()


def end_window():
    window.destroy()


def voice(texto):
    engine.say(texto)
    engine.runAndWait()


def print_tree(node, depth=0):
    if node is None:
        return
    print(" " * depth + "- " + node.question)
    print_tree(node.yes, depth + 2)
    print_tree(node.no, depth + 2)


if __name__ == '__main__':
    diseases = []
    question = ['¿Tiene fiebre?', '¿Tiene dolor de cabeza?', '¿Tiene Falta de aire?', '¿Tiene Mareo?',
                '¿Tiene Dolor muscular?', '¿Tiene Tos?']

#_---------------------------------------------Videos--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    videos = {
        "Influenza": "https://www.youtube.com/watch?v=hK5Oh3pWZyo",
        "Dengue": "https://www.youtube.com/watch?v=k2ohxoNUK9M",
        "Gripe": "https://www.youtube.com/watch?v=5uM7Z0xRBx4",
        "Neumonía": "https://www.youtube.com/watch?v=l1H7zDAOIU0",
        "Meningitis": "https://www.youtube.com/watch?v=wOtukS41qx4&pp=ygUKTWVuaW5naXRpcw%3D%3D",
        "Chikungunya": "https://www.youtube.com/watch?v=7wJddLVZrkY&pp=ygULQ2hpa3VuZ3VueWE%3D",
        "Virus del Nilo Occidental": "https://www.youtube.com/watch?v=G6V_uamtbcY&pp=ygUaRmllYnJlIGRlbCBOaWxvIE9jY2lkZW50YWw%3D",
        "Rubéola": "https://www.youtube.com/watch?v=7aOVAbzmRLM&pp=ygUIUnViw6lvbGE%3D",
        "Sarampión": "https://www.youtube.com/watch?v=ob4i_Zuz5gs&pp=ygUKU2FyYW1wacOzbg%3D%3D",
        "Varicela": "https://www.youtube.com/watch?v=-ZUXwugYHRc&pp=ygUIVmFyaWNlbGE%3D",
        "Herpes zóster": "https://www.youtube.com/watch?v=jvyrava-9ys&pp=ygUOSGVycGVzIHrDs3N0ZXI%3D",
        "Fiebre maculosa de las Montañas Rocosas": "https://www.youtube.com/watch?v=axIPLqZv8SI&pp=ygUoRmllYnJlIG1hY3Vsb3NhIGRlIGxhcyBNb250YcOxYXMgUm9jb3Nhcw%3D%3D",
        "Mononucleosis": "https://www.youtube.com/watch?v=dEq3c4_D95Y&pp=ygUNTW9ub251Y2xlb3Npcw%3D%3D",
        "Granulomatosis de Wegener": "https://www.youtube.com/watch?v=VSypfQelbSI&pp=ygUZR3JhbnVsb21hdG9zaXMgZGUgV2VnZW5lcg%3D%3D",
        "Linfoma": "https://www.youtube.com/watch?v=SpZLvrWKS3M&pp=ygUHTGluZm9tYQ%3D%3D",
        "Virus del Zika": "https://www.youtube.com/watch?v=1wimRQukTuE&pp=ygUOVmlydXMgZGVsIFppa2E%3D",
        "Paperas": "https://www.youtube.com/watch?v=Py2lyV-u7LQ&pp=ygUHUGFwZXJhcw%3D%3D",
        "Sarcoidosis": "https://www.youtube.com/watch?v=vxE94seT8mg&pp=ygULU2FyY29pZG9zaXM%3D",
        "Malaria": "https://www.youtube.com/watch?v=BrvJlhq_Ssk&pp=ygUHTWFsYXJpYQ%3D%3D",
        "Fiebre del dengue grave": "https://www.youtube.com/watch?v=0UeytAV3SNs&pp=ygUXRmllYnJlIGRlbCBkZW5ndWUgZ3JhdmU%3D",
        "Fiebre tifoidea": "https://www.youtube.com/watch?v=sZebtCEE6gc&pp=ygUPRmllYnJlIHRpZm9pZGVh",
        "Tifus": "https://www.youtube.com/watch?v=Mfc8iDc1LFA&pp=ygUFVGlmdXM%3D",
        "Asma": "https://www.youtube.com/watch?v=D9jH2OCjMgc&pp=ygUEQXNtYQ%3D%3D",
        "Fiebre Q": "https://www.youtube.com/watch?v=E0WjoH7UF8U&pp=ygUIRmllYnJlIFE%3D",
        "Brucelosis": "https://www.youtube.com/watch?v=t6fwpPJak-s&pp=ygUKQnJ1Y2Vsb3Npcw%3D%3D",
        "Fiebre del Nilo Occidental": "https://www.youtube.com/watch?v=dfAijoOmvZE&pp=ygUaRmllYnJlIGRlbCBOaWxvIE9jY2lkZW50YWw%3D",
        "Vasculitis": "https://www.youtube.com/watch?v=0Xvgg40HDtc&pp=ygUKVmFzY3VsaXRpcw%3D%3D",
        "Cáncer": "https://www.youtube.com/watch?v=74vGtHSfCT0&pp=ygUHQ8OhbmNlcg%3D%3D",
        "Escarlatina": "https://www.youtube.com/watch?v=NUYtHLBV6S0&pp=ygULRXNjYXJsYXRpbmE%3D",
        "Síndrome de shock tóxico": "https://www.youtube.com/watch?v=cBymrcSjiDE&pp=ygUaU8OtbmRyb21lIGRlIHNob2NrIHTDs3hpY28%3D",
        "Enfermedad de Hodgkin": "https://www.youtube.com/watch?v=ZlypjCxW4sM&pp=ygUVRW5mZXJtZWRhZCBkZSBIb2Rna2lu",
        "Enfermedad de Castleman": "https://www.youtube.com/watch?v=EXZgOsaHCoU&pp=ygUXRW5mZXJtZWRhZCBkZSBDYXN0bGVtYW4%3D",
        "Síndrome de Guillain-Barré": "https://www.youtube.com/watch?v=K8vKbiAZw8Y&pp=ygUcU8OtbmRyb21lIGRlIEd1aWxsYWluLUJhcnLDqQ%3D%3D",
        "Leptospirosis": "https://www.youtube.com/watch?v=it2nUhSTIj0&pp=ygUNTGVwdG9zcGlyb3Npcw%3D%3D",
        "Fibrosis quística": "https://www.youtube.com/watch?v=mhIhJtV1MsA&pp=ygUSRmlicm9zaXMgcXXDrXN0aWNh",
        "Anemia de células falciformes": "https://www.youtube.com/watch?v=_BNkerTPsLM&pp=ygUeQW5lbWlhIGRlIGPDqWx1bGFzIGZhbGNpZm9ybWVz",
        "VIH / SIDA": "https://www.youtube.com/watch?v=i7rqniyKfYk&pp=ygUKVklIIC8gU0lEQQ%3D%3D",
        "Talasemia": "https://www.youtube.com/watch?v=7vyZAO-AcwU&pp=ygUJVGFsYXNlbWlh",
        "Leucemia": "https://www.youtube.com/watch?v=vNF8RBiwIYo&pp=ygUITGV1Y2VtaWE%3D",
        "Fibrosis quística": "https://www.youtube.com/watch?v=mhIhJtV1MsA&pp=ygUSRmlicm9zaXMgcXXDrXN0aWNh",
        "Polimialgia reumática": "https://www.youtube.com/watch?v=ai6Z_WnjaV8&pp=ygUWUG9saW1pYWxnaWEgcmV1bcOhdGljYQ%3D%3D",
        "Enfermedad de Kawasaki": "https://www.youtube.com/watch?v=Ak3KLjV7ZRA&pp=ygUWRW5mZXJtZWRhZCBkZSBLYXdhc2FraQ%3D%3D",
        "Arteritis de células gigantes": "https://www.youtube.com/watch?v=42kldaUE1kY&pp=ygUeQXJ0ZXJpdGlzIGRlIGPDqWx1bGFzIGdpZ2FudGVz",
        "Enfermedad pulmonar asociada a polvo de madera": "https://www.youtube.com/watch?v=FPLHgQMiIf8&pp=ygUuRW5mZXJtZWRhZCBwdWxtb25hciBhc29jaWFkYSBhIHBvbHZvIGRlIG1hZGVyYQ%3D%3D",
        "Enfermedad de Lyme": "https://www.youtube.com/watch?v=wQgE06GAcyA&pp=ygUSRW5mZXJtZWRhZCBkZSBMeW1l",
        "Enfermedad pulmonar intersticial": "https://www.youtube.com/watch?v=d6RUvth_z6g&pp=ygUgRW5mZXJtZWRhZCBwdWxtb25hciBpbnRlcnN0aWNpYWw%3D",
        "Lupus eritematoso sistémico": "https://www.youtube.com/watch?v=wAvqTDieCw4",
        "Artritis reumatoide": "https://www.youtube.com/watch?v=IUef10P8zdk&pp=ygUTQXJ0cml0aXMgcmV1bWF0b2lkZQ%3D%3D",
        "Enfermedad pulmonar obstructiva crónica (EPOC)": "https://www.youtube.com/watch?v=V4GZM5fZhMg&t=0s&pp=ygUvRW5mZXJtZWRhZCBwdWxtb25hciBvYnN0cnVjdGl2YSBjcsOzbmljYSAoRVBPQyk%3D",
        "Aspergilosis pulmonar invasiva": "https://www.youtube.com/watch?v=pEYaC655LOs",
        "Bronquitis crónica": "https://www.youtube.com/watch?v=GISJp0zhySg&pp=ygUTQnJvbnF1aXRpcyBjcsOzbmljYQ%3D%3D",
        "Hepatitis C": "https://www.youtube.com/watch?v=d9x1bSYQ3vs&pp=ygULSGVwYXRpdGlzIEM%3D",
        "Diabetes mellitus": "https://www.youtube.com/watch?v=LhV3IZHFYA0&pp=ygURRGlhYmV0ZXMgbWVsbGl0dXM%3D",
        "Neumonitis por hipersensibilidad": "https://www.youtube.com/watch?v=xyn_VlSnqHY&pp=ygUgTmV1bW9uaXRpcyBwb3IgaGlwZXJzZW5zaWJpbGlkYWQ%3D",
        "Enfermedad pulmonar asociada a la hipersensibilidad al polvo de aves": "https://www.youtube.com/watch?v=azj52-XreSg&pp=ygVERW5mZXJtZWRhZCBwdWxtb25hciBhc29jaWFkYSBhIGxhIGhpcGVyc2Vuc2liaWxpZGFkIGFsIHBvbHZvIGRlIGF2ZXM%3D",
        "Enfermedad pulmonar asociada a la exposición a metales": "https://www.youtube.com/watch?v=azj52-XreSg&pp=ygVERW5mZXJtZWRhZCBwdWxtb25hciBhc29jaWFkYSBhIGxhIGhpcGVyc2Vuc2liaWxpZGFkIGFsIHBvbHZvIGRlIGF2ZXM%3D",
        "Insuficiencia cardíaca": "https://www.youtube.com/watch?v=i2-GbO6EZ7M&pp=ygUXSW5zdWZpY2llbmNpYSBjYXJkw61hY2E%3D",
        "Encefalitis": "https://www.youtube.com/watch?v=2eQxI9AQSbs&pp=ygULRW5jZWZhbGl0aXM%3D",
        "Enfermedad de Addison": "https://www.youtube.com/watch?v=w3iWNgVf3nI&pp=ygUVRW5mZXJtZWRhZCBkZSBBZGRpc29u",
        "Hepatitis B": "https://www.youtube.com/watch?v=DotrPy_8YW0&pp=ygULSGVwYXRpdGlzIEI%3D",
        "Enfermedad coronaria": "https://www.youtube.com/watch?v=lqcWtHXS_Cg&pp=ygUURW5mZXJtZWRhZCBjb3JvbmFyaWE%3D",
        "Hipotiroidismo": "https://www.youtube.com/watch?v=ZZHL7Rk7n-Q",
        "Enfermedad pulmonar asociada a la hipersensibilidad al polvo de tóner": "https://www.youtube.com/watch?v=azj52-XreSg&t=0s&pp=ygVGRW5mZXJtZWRhZCBwdWxtb25hciBhc29jaWFkYSBhIGxhIGhpcGVyc2Vuc2liaWxpZGFkIGFsIHBvbHZvIGRlIHTDs25lcg%3D%3D",
        "No tiene enfermedad": "https://www.youtube.com/watch?v=oM9fUlGET-w"

    }
#_-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    root = build_tree(question)


#_--------------------------------------------------------------Lectura de csv---------------------------------------------------------------------------------------------------------------------------------------------------------
    with open('enfermedades.csv', 'r', encoding="utf-8") as file:
        next(file, None)

        for line in file:
            line = line.rstrip()

            list = line.split(";")

            diseases.append(list)

#-------------------------------------------------------------Agregar Enfermedaes al arbol---------------------------------------------------------------------------------------------------------------------------------------------
    for i in range(len(diseases)):
        add_diseases(root, diseases, i)


    menu = True

    while menu:

#-----------------------------------------------------------Inicio del menu------------------------------------------------------------------------------------------------------------------------------------------------------------
        engine.say(f'¿Desea escuchar la introducción al programa? oprime la letra s para si, de lo contrario oprime la letra n')
        engine.runAndWait()

        x = input("¿Escuchar introducción? (s/n): ")
        if x.lower() == "s":
            engine.say(
                f'Un gusto hablar contigo señor usuario, soy Gio y soy tu asistente destinada para el programa de diagnosticación de enfermedades, espero serte de ayuda.')
            engine.runAndWait()
            engine.say(
                f'A continuación se te darán algunas preguntas sobre diferentes síntomas que puedes o no estar sufriendo, por favor, si sufres dicho síntoma entonces marca la casilla, de lo contrario, déjala sin marcar')
            engine.runAndWait()
        else:
            pass

    #-----------------------------------------------------Interfaz Grafica------------------------------------------------------------------------------------------------------------------------------------------------#
        window = tk.Tk()
        window.title("diagnosticación de enfermedades")
        window.geometry("300x250")

        answers = [tk.BooleanVar() for i in range(len(question))]

        tk.Label(window, text="diagnosticación de enfermedades").grid(row=0, column=0)
        tk.Label(window, text="").grid(row=1, column=0)

        for i in range(len(question)):
            tk.Label(window, text=question[i]).grid(row=i + 2, column=0)
            tk.Checkbutton(window, variable=tk.BooleanVar(value=False),
                           command=lambda i=i: answers.__setitem__(i, not answers[i])).grid(row=i + 2, column=1)
            tk.Button(window, text="🔊", command=lambda q=question[i]: voice(q)).grid(row=i + 2, column=2)

        tk.Label(window, text="").grid(row=8, column=0)
        tk.Button(window, text="Confirmar", command=end_window).grid(row=9, column=0)
        tk.Button(window, text="Instrucciones", command=lambda
            q='A continuación se te darán algunas preguntas sobre diferentes síntomas que puedes o no estar sufriendo, por favor, si sufres dicho síntoma entonces marca la casilla, de lo contrario, déjala sin marcar': voice(
            q)).grid(row=9, column=1)
        tk.Label(window, text="").grid(row=10, column=0)

        window.mainloop()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        travel(root, answers)


#-------------------------Repetición del Menu--------------------------------------------------------------------------------------------------------------------------------------------
        opc = input("¿Desea tomar el examen de nuevo? (s/n): ")

        if opc.lower() == "s":
            pass
        elif opc.lower() == "n":
            menu = False
            engine.say(f'Tenga feliz dia')
            engine.runAndWait()
