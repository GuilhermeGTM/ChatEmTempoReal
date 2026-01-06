from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Sala
from django.db.models import Q


def entrar(request):
    if request.method == 'GET':
        return render(request, 'entrar.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        apelido = request.POST.get('apelido')  # captura o apelido

        sala = Sala.objects.filter(Q(nome=nome) & Q(senha=senha)).first()

        if sala:
            # guarda na sessão que o usuário autenticou nesta sala
            request.session['sala_autenticada'] = sala.nome
            request.session['apelido'] = apelido
            return redirect(reverse('chat', args=(sala.nome, )))
        else:
            return HttpResponse('Nome ou senha inexistente')



def chat(request, nome):
    sala_autenticada = request.session.get('sala_autenticada')
    apelido = request.session.get('apelido')

    if sala_autenticada == nome and apelido:
        return render(request, 'chat.html', {'nome': nome, 'apelido': apelido})
    else:
        return HttpResponse('Acesso negado. Faça login na sala primeiro.')

