from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from .dummy_data import gadgets
from django.utils.text import slugify
from django.urls import reverse
import json

from django.views import View
from django.views.generic.base import RedirectView


# Create your views here.
def init_view(request):
    return render(request, 'gadget_list/test.html')

class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"
    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id", 0)]["name"])
        new_kwarg = {"gadget_slug": slug}
        return super().get_redirect_url(*args, **new_kwarg)

def single_gadget__int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("not found by me")


class GadgetView(View):
    def get(self, request, gadget_slug):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"received data: {data}")
            return JsonResponse({"response": "Das war wohl was"})
        except:
            return JsonResponse({"response": "Das war wohl nix"})


def single_gadget_view(request, gadget_slug=""):
    if request.method == "GET":
        gadget_match = None

        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"received data: {data}")
            return JsonResponse({"response": "Das war wohl was"})
        except:
            return JsonResponse({"response": "Das war wohl nix"})