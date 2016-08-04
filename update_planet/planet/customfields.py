# customfields.py https://djangosnippets.org/snippets/900/

from django import forms
from django.conf import settings
from django.db import models
from django.template.loader import render_to_string

class ColorWidget(forms.Widget):
    class Media:
        js = [settings.ADMIN_MEDIA_PREFIX + "js/ColorPicker2.js"]

    def render(self, name, value, attrs=None):
        return render_to_string("widget/color.html", locals())

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)

'''
# templates/widget/color.html

{% load common %}
<script type="text/javascript" charset="utf-8">
  var picker_{{ name }} = new ColorPicker('window');
</script>
<input type="text" readonly="true" tabindex="-1" size="2" style="background-color: {{ value }};" id="{{ attrs.id }}-sample"/>
<input type="text" name="{{ name }}" size="8" value="{{ value }}" id="{{ attrs.id }}" onChange="alert('changed');"/>
<a href="#" onclick="picker_{{ name }}.select(document.getElementById('{{ attrs.id }}'),document.getElementById('{{ attrs.id }}-sample'),'{{ attrs.id }}-pick');return false;" name="{{ attrs.id }}-pick" id="{{ attrs.id }}-pick">Pick</a>
<script type="text/javascript" charset="utf-8">
  picker_{{ name }}.writeDiv();
</script>
'''