from Shopping.models.orders import Order
from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
import json




class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})


class KhaltiRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)
        context = {
            "order": order
        }
        return render(request, "khaltirequest.html", context)


class KhaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        price = request.GET.get("price")
        o_id = request.GET.get("order_id")
        print(token, price, o_id)

        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "price": price
        }
        headers = {
            "Authorization": "Key test_secret_key_f59e8b7d18b4499ca40f68195a846e9b"
        }

        order_obj = Order.objects.get(id=o_id)

        response = request.post(url, payload, headers=headers)
        resp_dict = response.json()
        if resp_dict.get("idx"):
            success = True
            order_obj.payment_completed = True
            order_obj.save()
        else:
            success = False
        data = {
            "success": success
        }
        return JsonResponse(data)


def verify_payment(request):
    data = request.POST
    product_id = data['product_identity']
    token = data['token']
    price = data['price']

    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
        "token": token,
        "price": price
    }

    headers = {
        "Authorization": "Key test_secret_key_ec2594e8e4b24cc5abe9edbc874e3d85"
    }

    response = request.post(url, payload, headers=headers)

    response_data = json.loads(response.text)
    status_code = str(response.status_code)

    if status_code == '400':
        response = JsonResponse({'status': 'false', 'message': response_data['detail']}, status=500)
        return response

    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response_data)

    return JsonResponse(f"Payment Done !! With IDX. {response_data['user']['idx']}", safe=False)