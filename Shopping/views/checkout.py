from django.shortcuts import render, redirect
from Shopping.models.customer import Customer
from django.views import View
from Shopping.models.product import Product
from Shopping.models.orders import Order
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.mail import EmailMultiAlternatives


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))

        ordered_products = []
        grand_total = 0  # New variable for total sum

        for product in products:
            quantity = cart.get(str(product.id))
            total = product.price * quantity
            grand_total += total  # Add to grand total

            order = Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                address=address,
                email=email,
                phone=phone,
                fullname=fullname,
                quantity=quantity
            )
            order.save()

            ordered_products.append({
                'name': product.name,
                'price': product.price,
                'quantity': quantity,
                'total': total,
            })

        subject = 'Order Successfully Created!'
        from_email = 'Sirutarfutsal2018@gmail.com'
        to = [email]
        text_content = f'Hi {fullname}, your order has been confirmed!'

        html_content = render_to_string('orderemail_template.html', {
            'fullname': fullname,
            'phone': phone,
            'address': address,
            'ordered_products': ordered_products,
            'grand_total': grand_total,  # Pass total to template
        })

        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        request.session['cart'] = {}

        return redirect('orders')



def sendordermail(request):
    send_mail(
        'New Order have been placed.',
        'This mail is to inform you that new orders have been placed by a customer. Please check your admin dashboard and confirm all orders.',
        'Sirutarfutsal2018@gmail.com',
        ['numb1prabesht7@gmail.com'],
        fail_silently=False,
    )
    return redirect('orders')


def orders_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    orders = Order.objects.all()
    lines = []
    for order in orders:
        lines.append(order.fullname)
        lines.append(order.address)
        lines.append(order.phone)
        lines.append(order.email)
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='orders.pdf')
