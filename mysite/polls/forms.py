# -*- coding: utf-8 -*-
from django import forms

from .models import Usb


class Usbform(forms.ModelForm):

    class Meta:
        model = Usb
        fields = ('name','readspeed','price')


class Usbform2(forms.ModelForm):

    class Meta:
        model = Usb
        fields = ('readspeed',)