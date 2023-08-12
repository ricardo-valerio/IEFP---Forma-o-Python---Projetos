from django.contrib import admin

from .models import TipoDeAnimal, Raca, Idade, PorteTamanho,     \
					CorDoPelo, ZonasDoPais, AnuncioAnimal,  	 \
					AssociacoesDeAnimais, Faq, SobreProjeto,     \
					MedidasParaAjudar


class TipoDeAnimalAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(TipoDeAnimal, TipoDeAnimalAdmin)


class RacaAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(Raca, RacaAdmin)


class IdadeAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(Idade, IdadeAdmin)


class PorteTamanhoAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(PorteTamanho, PorteTamanhoAdmin)


class CorDoPeloAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(CorDoPelo, CorDoPeloAdmin)


class ZonasDoPaisAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(ZonasDoPais, ZonasDoPaisAdmin)


class AnuncioAnimalAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(AnuncioAnimal, AnuncioAnimalAdmin)


class AssociacoesDeAnimaisAdmin(admin.ModelAdmin):
	list_display = ('nome', 'localidade', 'id_zona_do_pais_fk', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(AssociacoesDeAnimais, AssociacoesDeAnimaisAdmin)


class FaqAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(Faq, FaqAdmin)


class SobreProjetoAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(SobreProjeto, SobreProjetoAdmin)

class MedidasParaAjudarAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	readonly_fields = ('id',)
	ordering = ['id']
admin.site.register(MedidasParaAjudar, MedidasParaAjudarAdmin)

