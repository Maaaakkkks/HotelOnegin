from dataclasses import fields
from pyexpat import model
from django import forms

from booking.models import Booking


class Booking(model.Booking):
    class Meta:
        model = Booking
        fields = (
            "date_in",
            "date_out",
            "person",
            "child",)

    date_in = forms.CharField()
    date_out = forms.CharField()
    persom = forms.CharField()
    child = forms.CharField()