from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),

    # ex: adoptar/5
    path("adoptar/<int:anuncio_id>", views.adoptar, name="adoptar"),

    path("anunciar", views.anunciar, name="anunciar"),
    path("associacoes", views.associacoes, name="associacoes"),
    path("faq", views.faq, name="faq"),
    path("como-ajudar", views.como_ajudar, name="como_ajudar"),
    path("sobre-o-projecto", views.sobre_o_projecto, name="sobre_o_projecto"),

    path("procurar", views.procurar, name="procurar"),
    path("filtrar", views.filtrar, name="filtrar"),
    path("accounts/signup", views.SignUpView.as_view(), name="signup"),

    path("meus-anuncios", views.meus_anuncios, name="meus_anuncios"),
    path("eliminar-anuncio/<int:anuncio_id>", views.eliminar_anuncio, name="eliminar_anuncio"),
    path("editar-anuncio/<int:anuncio_id>", views.editar_anuncio, name="editar_anuncio"),

]
