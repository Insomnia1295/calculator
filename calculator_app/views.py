from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .calculator import Calculator
from .forms import CalculatorForm
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView


# Function based view:
#def calculator_view(request):
#   if request.method == 'POST':
 #       calculator=Calculator()
  #      calculator.number1= float(request.POST['number1'])
   #     calculator.number2 = float(request.POST['number2'])
    #    function= request.POST['function']

     #   if function == '+':
      #      result = calculator.addition()
       # elif function == '-':
        #    result = calculator.subtraction()
  #      elif function == '*':
   #         result = calculator.multiplication()
    #    elif function == '/':
     #       if calculator.number1 == 0 or calculator.number2 == 0:
      #          result = None
       #         error_message = "Error: Cannot divide by zero."
        #    else:
         #       result = calculator.division()
          #      error_message = None
      #  else:
       #     result = None
        #    error_message= "Error: Invalid function."
        #return render(request, 'calculator_app/result.html', {'result': result})

  #  background_image="calculatorimg.jpg"

   # return render(request, 'calculator_app/calculator_form.html', {'background_image': background_image})

   # return render(request, 'calculator_app/calculator_form.html')


# Class Based View:

class CalculatorView(FormView):
    template_name = 'calculator_app/calculator_form.html'
    form_class = CalculatorForm
    success_url = reverse_lazy('calculator')

    def form_valid(self, form):
        calculator = Calculator()
        calculator.number1 = form.cleaned_data['number1']
        calculator.number2 = form.cleaned_data['number2']
        function = form.cleaned_data['function']

        if function == '+':
            result = calculator.addition()
            error_message = None
        elif function == '-':
            result = calculator.subtraction()
            error_message = None
        elif function == '*':
            result = calculator.multiplication()
            error_message = None
        elif function == '/':
            if calculator.number2 == 0:
                result = None
                error_message = 'Error: cannot divide by 0'
            else:
                result = calculator.division(calculator.number1, calculator.number2)
                error_message = None
        else: 
            result = None
            error_message = 'Error: Invalid function.'
    
        background_image = "calculatorimg.jpg"

        if result is not None:
            return render(self.request, 'calculator_app/result.html', {'result': result, 'error_message': error_message})
        else:
            return render(self.request, 'calculator_app/calculator_form.html', {'background_image': background_image, 'error_message': error_message})

#APIview:
class CalculatorAPI(APIView):
    def post(self, request, *args, **kwargs):
        number1 = float(request.data.get('number1', 0))
        number2 = float(request.data.get('number2', 0))
        function = request.data.get('function')

        if function == '+':
            result = number1 + number2
        elif function == '-':
            result = number1 - number2
        elif function == '*':
            result = number1 * number2
        elif function == '/':
            if number2 != 0:
                result = number1 / number2
            else:
                return Response({'error': 'Cannot divide by zero'}, status=400)
        else:
            return Response({'error': 'Invalid function'}, status=400)

        return Response({'result': result})