from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PlsNM1dQ5ksTGhXduAl3Se0nx4g824qDBHltETSgSV55wJhh7hug2r3Vo4WmFXxYf5YAln78UTeflGNdmItJ6Rk00Y09eAJne',
        'client_secret': 'sk_test_51PlsNM1dQ5ksTGhXsEIIq4kxIUR99rbga4mdl5S1S4VEdoheGIufEsPaw8aWxUpWJQlxZRvo9aflGebJhQBxiI7B00QVx8b4gG',
    }

    return render(request, template, context)
