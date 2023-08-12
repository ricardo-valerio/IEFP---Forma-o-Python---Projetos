from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .models import *
from pprint import pprint
import operator
from functools import reduce


NUMERO_DE_ANIMAIS_NO_PAGINADOR = 9

# Este é o padrão: -------------------------------------------------------------
# importar o Model
# from .models import Question
#
# Fazer uma query in passar para a view como contexto numa variável
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)
# ------------------------------------------------------------------------------

def index(request):
    # Animais
    # animais_values = AnuncioAnimal.objects.select_related('id_tipo_de_animal_fk').all().order_by('datetime_anuncio').values()
    animais = AnuncioAnimal.objects.filter(anuncio_estado=True).order_by('-datetime_anuncio')
    paginator = Paginator(animais, NUMERO_DE_ANIMAIS_NO_PAGINADOR)
    page_number = request.GET.get("page")
    animais = paginator.get_page(page_number)
    # LEFT SEARCH PANEL -------------------------------------------------
    zonas_do_pais  = ZonasDoPais.objects.all()
    tipo_de_animal = TipoDeAnimal.objects.all()
    raca           = Raca.objects.all()
    idade          = Idade.objects.all()
    porte_tamanho  = PorteTamanho.objects.all()
    cor_do_pelo    = CorDoPelo.objects.all()

    context = {
        # 'animais_values': animais_values,
        'animais'        : animais,
        'zonas_do_pais'  : zonas_do_pais,
        'tipo_de_animal' : tipo_de_animal,
        'raca'           : raca,
        'idade'          : idade,
        'porte_tamanho'  : porte_tamanho,
        'cor_do_pelo'    : cor_do_pelo,
        'request'        : request,
    }
    return render(request, "animais_para_adocao/index.html", context)

def adoptar(request, anuncio_id):
    animal = get_object_or_404(AnuncioAnimal, pk=anuncio_id)
    context = {'animal': animal}
    return render(request, "animais_para_adocao/adoptar.html", context)



from .forms import AnunciarForm

def anunciar(request):
    form = AnunciarForm(request.POST or None, request.FILES or None, initial={'user': request.user.id})

    if form.is_valid():
        print("entrou aqui")
        form.save()
        return redirect('index')

    context = {
        'form' : form,
    }

    return render(request, "animais_para_adocao/anunciar.html", context)




def associacoes(request):
    associacoes = AssociacoesDeAnimais.objects.all()
    zonas_do_pais = ZonasDoPais.objects.all()
    context = {'associacoes': associacoes, 'zonas_do_pais': zonas_do_pais}
    return render(request, "animais_para_adocao/associacoes.html", context)

def faq(request):
    faqs = Faq.objects.all()
    context = {'faqs': faqs}
    return render(request, "animais_para_adocao/faq.html", context)

def como_ajudar(request):
    medidas = MedidasParaAjudar.objects.all()
    context = {'medidas': medidas}
    return render(request, "animais_para_adocao/como_ajudar.html", context)

def sobre_o_projecto(request):
    sobre = SobreProjeto.objects.get(pk=1)
    context = {'sobre': sobre}
    return render(request, "animais_para_adocao/sobre_o_projecto.html", context)

def procurar(request):
    animais = AnuncioAnimal.objects.filter(
                    Q(anuncio_estado=True) &
                    Q(nome__contains=request.GET['q'])     |
                    Q(descricao_do_animal__contains=request.GET['q'])
              )
    paginator = Paginator(animais, NUMERO_DE_ANIMAIS_NO_PAGINADOR)
    page_number = request.GET.get("page")
    animais = paginator.get_page(page_number)

    # LEFT SEARCH PANEL -------------------------------------------------
    zonas_do_pais  = ZonasDoPais.objects.all()
    tipo_de_animal = TipoDeAnimal.objects.all()
    raca           = Raca.objects.all()
    idade          = Idade.objects.all()
    porte_tamanho  = PorteTamanho.objects.all()
    cor_do_pelo    = CorDoPelo.objects.all()

    mensagem = "Não foram encontrados resultados com esses critérios de pesquisa...por favor tente de novo!"

    context = {
        'animais'        : animais,
        'zonas_do_pais'  : zonas_do_pais,
        'tipo_de_animal' : tipo_de_animal,
        'raca'           : raca,
        'idade'          : idade,
        'porte_tamanho'  : porte_tamanho,
        'cor_do_pelo'    : cor_do_pelo,
        'mensagem'       : mensagem,
    }

    return render(request, "animais_para_adocao/index.html", context)

def filtrar(request):
    # pprint(request.GET)
    if request.GET:
        query_list = [Q(anuncio_estado=True)]
        if request.GET['zonas_do_pais'] != '-1':
            query_list.append(Q(id_zona_do_pais_fk_id=request.GET['zonas_do_pais']))

        if request.GET['tipo_de_animal'] != '-1':
            query_list.append(Q(id_tipo_de_animal_fk_id=request.GET['tipo_de_animal']))

        if request.GET['raca'] != '-1':
            query_list.append(Q(id_raca_fk_id=request.GET['raca']))

        if request.GET['idade'] != '-1':
            query_list.append(Q(id_idade_fk_id=request.GET['idade']))

        if request.GET['sexo'] != '-1':
            query_list.append(Q(sexo=request.GET['sexo']))

        if request.GET['porte_tamanho'] != '-1':
            query_list.append(Q(id_porte_tamanho_fk_id=request.GET['porte_tamanho']))

        if request.GET['cor_do_pelo'] != '-1':
            query_list.append(Q(id_cor_do_pelo_fk_id=request.GET['cor_do_pelo']))

    # LEFT SEARCH PANEL -------------------------------------------------
    animais = AnuncioAnimal.objects.filter(reduce(operator.and_, query_list)).order_by('-datetime_anuncio') if len(query_list) > 0 else AnuncioAnimal.objects.filter(anuncio_estado=True).order_by('-datetime_anuncio')
    paginator = Paginator(animais, NUMERO_DE_ANIMAIS_NO_PAGINADOR)
    page_number = request.GET.get("page")
    animais = paginator.get_page(page_number)

    zonas_do_pais  = ZonasDoPais.objects.all()
    tipo_de_animal = TipoDeAnimal.objects.all()
    raca           = Raca.objects.all()
    idade          = Idade.objects.all()
    porte_tamanho  = PorteTamanho.objects.all()
    cor_do_pelo    = CorDoPelo.objects.all()

    mensagem = "Não foram encontrados resultados com esses critérios de pesquisa! <br><br> Por favor tente de novo!"

    context = {
        'animais'        : animais,
        'zonas_do_pais'  : zonas_do_pais,
        'tipo_de_animal' : tipo_de_animal,
        'raca'           : raca,
        'idade'          : idade,
        'porte_tamanho'  : porte_tamanho,
        'cor_do_pelo'    : cor_do_pelo,
        'mensagem'       : mensagem,
    }

    return render(request, "animais_para_adocao/index.html", context)





from django.contrib.auth.decorators import login_required

@login_required
def meus_anuncios(request):
    meus_anuncios = AnuncioAnimal.objects.filter(user_id=request.user.id).order_by('-datetime_anuncio')
    context = {
        'user_id': request.user.id,
        'meus_anuncios': meus_anuncios
    }
    return render(request, "animais_para_adocao/meus_anuncios.html", context)


@login_required
def eliminar_anuncio(request, anuncio_id):
    anuncio = AnuncioAnimal.objects.get(pk=anuncio_id)
    anuncio.delete()
    return redirect('meus_anuncios')


from .forms import EditarAnuncioForm

@login_required
def editar_anuncio(request, anuncio_id):
    anuncio = AnuncioAnimal.objects.get(pk=anuncio_id)
    if request.method == 'POST':
        form = EditarAnuncioForm(request.POST, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect('meus_anuncios')
    else:
        form = EditarAnuncioForm(instance=anuncio)
        context = {'form': form, 'anuncio_id': anuncio.id}
        return render(request, "animais_para_adocao/editar_anuncio.html", context)





from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].label = "Endereço de E-mail"
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].label = "Confirmação de Password"


        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username", "email")

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    # pprint(dir(form_class))
    # pprint(vars(form_class))

    form_class.fields = ("username", "email")
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
