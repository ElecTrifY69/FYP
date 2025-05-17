from django.shortcuts import render, redirect
from Infofutsal.models.review import Review
from django.contrib import messages
from django.views import View
from Shopping.models.customer import Customer


class review(View):
    def get(self, request):
        customer = Customer.get_all_customers()
        review_list = Review.get_all_reviews()
        return render(request, 'review.html', {'customer': customer, 'review_list': review_list})

    def post(self, request):
        review = Review()
        fullname = request.POST.get('fullname')
        message = request.POST.get('message')
        if len(request.FILES) != 0:
            review.photo = request.FILES['photo']
        #photo = request.POST.get('photo')
        review.fullname = fullname
        review.message = message
        review.save()
        messages.success(request, 'Your Review has been successfully added on About Us page!', extra_tags='review')
        return redirect('aboutus')
