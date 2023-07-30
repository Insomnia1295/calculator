from django.shortcuts import render

from .calculator import Calculator

def calculator_view(request):
    if request.method == 'POST':
        calculator=Calculator()
        calculator.number1= float(request.POST['number1'])
        calculator.number2 = float(request.POST['number2'])
        function= request.POST['function']

        if function == '+':
            result = calculator.addition()
        elif function == '-':
            result = calculator.subtraction()
        elif function == '*':
            result = calculator.multiplication()
        elif function == '/':
            if calculator.number1 == 0 or calculator.number2 == 0:
                result = None
                error_message = "Error: Cannot divide by zero."
            else:
                result = calculator.division()
                error_message = None
        else:
            result = None
            error_message= "Error: Invalid function."
        return render(request, 'calculator_app/result.html', {'result': result})

    background_image="calculatorimg.jpg"

    return render(request, 'calculator_app/calculator_form.html', {'background_image': background_image})

    return render(request, 'calculator_app/calculator_form.html')
