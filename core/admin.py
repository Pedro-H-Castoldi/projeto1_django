from django.contrib import admin

from .models import Cliente, Produto

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
