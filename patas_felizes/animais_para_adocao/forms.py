from django import forms
from .models import AnuncioAnimal
import pprint


class AnunciarForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nome'].widget.attrs.update({"class": "form-control my-2"})
		self.fields['id_tipo_de_animal_fk'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['id_raca_fk'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['id_idade_fk'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['id_porte_tamanho_fk'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['id_cor_do_pelo_fk'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['sexo'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['imagem'].widget.attrs.update({"class": "form-control my-2"})
		self.fields['descricao_do_animal'].widget.attrs.update({"class": "form-control my-2", 'rows': 7})
		self.fields['esterilizado'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['vacinado'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['desparasitado'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['user'].widget.attrs.update({"class": "form-control my-2"})
		self.fields['nome_anunciante'].widget.attrs.update({"class": "form-control my-2"})
		self.fields['id_zona_do_pais_fk'].widget.attrs.update({"class": "form-select my-2"})
		self.fields['localidade_anunciante'].widget.attrs.update({"class": "form-control my-2"})
		self.fields['contacto_telefonico_anunciante'].widget.attrs.update({"class": "form-control my-2"})
		self.fields['email_anunciante'].widget.attrs.update({"class": "form-control my-2"})
		self.fields['anuncio_estado'].widget.attrs.update({"class": "my-3"})

	class Meta:
		model = AnuncioAnimal
		fields = "__all__"
		widgets = {
			'user': forms.HiddenInput(),
			'anuncio_estado': forms.HiddenInput(),
		}



class EditarAnuncioForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	        super().__init__(*args, **kwargs)
	        self.fields['nome'].widget.attrs.update({"class": "form-control my-2"})
	        self.fields['id_tipo_de_animal_fk'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['id_raca_fk'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['id_idade_fk'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['id_porte_tamanho_fk'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['id_cor_do_pelo_fk'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['sexo'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['imagem'].widget.attrs.update({"class": "form-control my-2"})
	        self.fields['descricao_do_animal'].widget.attrs.update({"class": "form-control my-2", 'rows': 7})
	        self.fields['esterilizado'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['vacinado'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['desparasitado'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['user'].widget.attrs.update({"class": "form-control my-2"})
	        self.fields['nome_anunciante'].widget.attrs.update({"class": "form-control my-2"})
	        self.fields['id_zona_do_pais_fk'].widget.attrs.update({"class": "form-select my-2"})
	        self.fields['localidade_anunciante'].widget.attrs.update({"class": "form-control my-2"})
	        self.fields['contacto_telefonico_anunciante'].widget.attrs.update({"class": "form-control my-2"})
	        self.fields['email_anunciante'].widget.attrs.update({"class": "form-control my-2"})
	        self.fields['anuncio_estado'].widget.attrs.update({"class": "my-3"})


	class Meta:
		model = AnuncioAnimal
		fields = "__all__"
		widgets = {
			'user': forms.HiddenInput(),
		}
