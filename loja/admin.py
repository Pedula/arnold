from django.contrib import admin
from loja.models import Usuario, Produto, Pedido

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Produto)
admin.site.register(Pedido)