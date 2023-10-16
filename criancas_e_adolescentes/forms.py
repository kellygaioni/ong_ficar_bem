from django import forms
from criancas_e_adolescentes.models import Crianca_e_Adolescente

class Crianca_e_AdolescenteForm(forms.ModelForm):
    class Meta:
        model = Crianca_e_Adolescente
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo",
        ]

        error_messages = {
            "nome_completo": {
                "required": "O nome completo é obrigatório para o registro",
            },
            "cpf": {
                "required": "O CPF é obrigatório para o registro"
            },
            "data_nascimento": {
                "required": "A data de nascimento  é obrigatória para o registro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA)"
            },
            "numero_casa": {
                "required": "Por favor, informe o número da casa a ser visitada"
            }
        }