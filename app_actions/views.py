from django.shortcuts import render


def inicio(request):
    resultado = None

    if request.method == "POST":
        try:
            numero1 = float(request.POST.get("numero1", 0))
            numero2 = float(request.POST.get("numero2", 0))
            operacion = request.POST.get("operacion")

            if operacion == "sumar":
                resultado = numero1 + numero2
            elif operacion == "restar":
                resultado = numero1 - numero2

        except (ValueError, TypeError):
            resultado = "Ingresa dos números válidos"

    return render(
        request,
        "app_actions/calculadora.html",
        {"resultado": resultado}
    )
