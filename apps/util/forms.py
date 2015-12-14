from django import forms
from .models import Interested
from django.utils.translation import ugettext_lazy as _


class RegisterInterestedForm(forms.ModelForm):

    class Meta:
        model = Interested
        fields = ('email', 'seller', 'buyer', 'android', 'ios')
        labels = {
            'seller': _('Quiero vender'),
            'buyer': _('Quiero comprar'),
        }
        #help_texts = {
        #    'email': _('Ingresa tu email para obtener las ultimas novedades de CompraloAhí.'),
        #}
        error_messages = {
            'email': {
                'required': _("Para poder recibir informacion sobre compraloahi el email es obligatorio"),
                'unique': _("El email ingresado ya esta registrado.")
            },
        }

    def clean(self):

        if not self.cleaned_data.get('seller') and not self.cleaned_data.get('buyer'):
            self.add_error('seller', "")
            self.add_error('buyer', "Elegi que quieres hacer con la plataforma, si quieres comprar y/o vender.")

        return super(RegisterInterestedForm, self).clean()


from django.core.mail import EmailMultiAlternatives

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)


    def send_email(self):
        # send email using the self.cleaned_data dictionary
        name = self.cleaned_data.get('name', '')
        email = self.cleaned_data.get('email', '')
        message = self.cleaned_data.get('message', '')

        html_content = "Datos de contactos : contacto : "+ name + " email : " + email +  " mensaje : " + message
        msg = EmailMultiAlternatives('Contact by page Compraloahi',
                                          html_content,
                                          'notificacion@compraloahi.com.ar',
                                          [ 'contextinformatic@gmail.com'])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()