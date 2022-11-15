from django.test import TestCase
from things.forms import ThingsForm
from things.models import Thing
from django import forms

class ThingsFormTestCase(TestCase):
    """Unit tests for the things form"""

    def setUp(self):
        self.form_input = {
            'name' : 'Jereon Keppens',
            'description' : 'A very nice man',
            'quantity' : 1
        }

    #valid input data
    def test_valid_ThingsForm(self):
        form = ThingsForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    #has neccessary fields
    def test_form_has_neccessary_fields(self):
        form = ThingsForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('quantity', form.fields)
        quantity_field = form.fields['quantity']
        self.assertTrue(isinstance(quantity_field, forms.IntegerField))

    #uses model validation
    def test_form_uses_model_validation(self):
        self.form_input['name'] = 'x' * 36
        self.form_input['quantity'] = -1
        form = ThingsForm(data = self.form_input)
        self.assertFalse(form.is_valid())
