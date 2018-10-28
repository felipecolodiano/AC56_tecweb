from django import forms

class ContatoForm(forms.Form):

    email = forms.EmailField()
    nome = forms.CharField()
    assunto = forms.CharField()
    mensagem = forms.CharField()

    def is_valid(self):
        valido = super(ContatoForm, self).is_valid()
        if valido :
            self.enviar_email()
        return valido

    def enviar_email(self):
        print("Nome: "+self.cleaned_data["nome"])
        print("Email: "+self.cleaned_data["email"])
        print("Assunto: "+self.cleaned_data["assunto"])
        print("Mensagem:")
        print(self.cleaned_data["mensagem"])


