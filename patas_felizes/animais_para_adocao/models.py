from django.db import models
from django.contrib.auth.models import User


class TipoDeAnimal(models.Model):
	tipo = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = "Tipo De Animal"

	def __str__(self):
		return self.tipo


class Raca(models.Model):
	raca 			  = models.CharField(max_length=50)
	tipo_de_animal_fk = models.ForeignKey(TipoDeAnimal, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Raça"


	def __str__(self):
		return self.raca


class Idade(models.Model):
	idade = models.CharField(max_length=20)

	class Meta:
		verbose_name_plural = "Idade"


	def __str__(self):
		return self.idade


class PorteTamanho(models.Model):
	porte_tamanho = models.CharField(max_length=20)

	class Meta:
		verbose_name_plural = "Porte / Tamanho"


	def __str__(self):
		return self.porte_tamanho


class CorDoPelo(models.Model):
	cor_do_pelo = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = "Cor do Pêlo"


	def __str__(self):
		return self.cor_do_pelo


class ZonasDoPais(models.Model):
	zona_do_pais = models.CharField(max_length=20, verbose_name="Zona do País")

	class Meta:
		verbose_name_plural = "Zona Do País"


	def __str__(self):
		return self.zona_do_pais


class AnuncioAnimal(models.Model):
	nome                  = models.CharField(max_length=20)

	id_tipo_de_animal_fk  = models.ForeignKey(TipoDeAnimal, on_delete=models.CASCADE)
	id_raca_fk            = models.ForeignKey(Raca, on_delete=models.CASCADE)
	id_idade_fk           = models.ForeignKey(Idade, on_delete=models.CASCADE)
	id_porte_tamanho_fk   = models.ForeignKey(PorteTamanho, on_delete=models.CASCADE)
	id_cor_do_pelo_fk     = models.ForeignKey(CorDoPelo, on_delete=models.CASCADE)

	sexo                  = models.CharField(max_length=10, choices=[('1', "Fêmea"), ('2', "Macho")])
	imagem                = models.ImageField(upload_to='imagens/animais/', blank=False)
	descricao_do_animal   = models.TextField()

	esterilizado = models.CharField(
		max_length=10,
		choices=[
			('1', "Esterilizado"),
			('2', "Não Esterilizado"),
			('3', "Desconhecido")
		]
	)

	vacinado = models.CharField(
		max_length=10,
		choices=[
			('1', "Vacinas em Dia"),
			('2', "Algumas Vacinas"),
			('3', "Não Vacinado"),
			('4', "Desconhecido")
		]
	)

	desparasitado = models.CharField(
		max_length=10,
		choices=[
			('1', "Desparasitado"),
			('2', "Não Desparasitado"),
			('3', "Desconhecido")
		]
	)

	user 						   = models.ForeignKey(User, on_delete=models.CASCADE)
	nome_anunciante                = models.CharField(max_length=50)
	id_zona_do_pais_fk             = models.ForeignKey(ZonasDoPais, on_delete=models.CASCADE)
	localidade_anunciante          = models.CharField(max_length=20)
	contacto_telefonico_anunciante = models.CharField(max_length=9)
	email_anunciante               = models.CharField(max_length=100)
	datetime_anuncio               = models.DateTimeField(auto_now_add=True)
	anuncio_estado 				   = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = "Anúncio do Animal"


	def __str__(self):
		return f" Anúncio com id: {self.id} | animal com nome: {self.nome}"


class AssociacoesDeAnimais(models.Model):
	nome                   = models.CharField(max_length=50)
	id_zona_do_pais_fk     = models.ForeignKey(ZonasDoPais, on_delete=models.CASCADE, verbose_name="Zona do País")
	localidade             = models.CharField(max_length=30)
	website_ou_rede_social = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Associações de Animais"


	def __str__(self):
		return self.nome

class Faq(models.Model):
	pergunta = models.CharField(max_length=300)
	resposta = models.TextField()

	class Meta:
		verbose_name_plural = "Faq"


	def __str__(self):
		return self.pergunta


class SobreProjeto(models.Model):
	descricao      = models.TextField()
	autor          = models.CharField(max_length=50)
	agradecimentos = models.TextField()

	class Meta:
		verbose_name_plural = "Sobre o Projeto"


	def __str__(self):
		return f"Sobre o Projecto | Autor {self.autor}"


class MedidasParaAjudar(models.Model):
	medida_titulo = models.CharField(max_length=100)
	medida_texto = models.TextField()

	class Meta:
		verbose_name_plural = "Medidas para Ajudar"


	def __str__(self):
		return self.medida_titulo
