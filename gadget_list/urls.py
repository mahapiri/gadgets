from django.urls import path
from .views import init_view, single_gadget__int_view, RedirectToGadgetView, GadgetView, init_view


urlpatterns = [
    path('start/', init_view),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget__int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),
]