from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from .models import Calculator

class CalculatorAPI(APIView):
    def post(self, request):
        number1 = request.data.get('number1')
        number2 = request.data.get('number2')
        function = request.data.get('function')

        calculator = Calculator(number1=number1, number2=number2)

        if function == '+':
            result = calculator.addition()
        elif function == '-':
            result = calculator.subtraction()
        elif function == '*':
            result = calculator.multiplication()
        elif function == '/':
            if calculator.number2 == 0:
                return Response({"error": "Cannot divide by zero"}, status=status.HTTP_400_BAD_REQUEST)
            result = calculator.division()
        else:
            return Response({"error": "Invalid function"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"result": result}, status=status.HTTP_200_OK)
