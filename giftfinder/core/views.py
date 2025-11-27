from django.shortcuts import render
from .forms import GiftSearchForm
from .utils import get_gift_suggestions


def gift_finder_view(request):
    form = GiftSearchForm(request.GET or None)
    gifts = []

    if form.is_valid():
        criteria = form.cleaned_data
        gifts = get_gift_suggestions(criteria)

    context = {
        "form": form,
        "gifts": gifts,
    }
    return render(request, "gift_finder.html", context)
