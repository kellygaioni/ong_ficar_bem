from django.db import models

class Adm(models.Model):

# Todo ADM é um usuário
    usuario = models.OneToOneField(
        "usuarios.Usuario",
        verbose_name="Usuário",
        on_delete=models.CASCADE
    )

    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name="Telefone de contato",
        max_length=11,
    )

    data_nascimento = models.DateField(
    verbose_name="Data de nascimento",
    auto_now_add=False,
    auto_now=False
    )

    class Meta:
        verbose_name = "Adm"
        verbose_name_plural = "Adms"
        db_table = "adm"

    def __str__(self):
        return self.nome_completo