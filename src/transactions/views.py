from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from transactions.models import Transaction
from django.db import IntegrityError
from transactions.serializers import TransactionSerializer
from django.db.models import Sum, Q


class TransactionView(APIView):


    def get(self, request, pk=None):
        if pk is None:
            return self.get_all(request)
        else:
            return self.get_one(pk)


    def get_all(self, request):
        group_by = request.query_params.get('group_by')

        if group_by == 'type':
            results = Transaction.objects.values('email').annotate(
                total_inflow=Sum('amount', filter=Q(type='inflow')),
                total_outflow=Sum('amount', filter=Q(type='outflow'))
            ).values('email', 'total_inflow', 'total_outflow')

            return JsonResponse(list(results), safe=False)
        else:
            transactions = Transaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            return JsonResponse(serializer.data)


    def get_one(self, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
            serializer = TransactionSerializer(transaction)
            return JsonResponse(serializer.data)
        except Transaction.DoesNotExist:
            return HttpResponse(status=404)


    def post(self, request):
        data = JSONParser().parse(request)
        response = []

        try:
            if isinstance(data, list):
                response = [save_transaction(transaction) for transaction in data]
            elif isinstance(data, dict):
                response = save_transaction(data)

            return JsonResponse(response, safe=False, status=201)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=400)

    
    def put(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return HttpResponse(status=404)

        data = JSONParser().parse(request)
        try:
            response = save_transaction(data, transaction)
            return JsonResponse(response, status=201)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=400)


    def delete(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return HttpResponse(status=404)

        transaction.delete()
        return HttpResponse(status=204)


    def summary(request, email):
        summary = Transaction.objects.filter(email=email).values('category').annotate(
            total_inflow=Sum('amount', filter=Q(type='inflow')),
            total_outflow=Sum('amount', filter=Q(type='outflow'))
        )

        return JsonResponse(list(summary), safe=False)


def save_transaction(data, transaction=None):

    if transaction is not None:
        transaction_serializer = TransactionSerializer(transaction, data=data)
    else:
        transaction_serializer = TransactionSerializer(data=data)

    if not transaction_serializer.is_valid():
        raise Exception(transaction_serializer.errors)

    try:
        transaction_serializer.save()
        return transaction_serializer.data
    except IntegrityError as e:
        raise Exception({"non_field_errors": ["Transaction already exist"]})
    except:
        raise Exception({"non_field_errors": ["Error to save transaction"]})
