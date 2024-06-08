from django.contrib import admin

from .models import Produto, Doacao, DoacaoItem, Entrega, Entrega_Item

admin.site.register(Produto)
admin.site.register(Doacao)
admin.site.register(DoacaoItem)
admin.site.register(Entrega)
admin.site.register(Entrega_Item)
