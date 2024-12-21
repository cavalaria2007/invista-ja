
#Formulario que estamos utilizando
from django.forms import ModelForm
# todos os modelos e classes que representam tabelas no banco de dados, elas estao dentro de models
from .models import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        

