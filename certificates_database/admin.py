from django.contrib import admin
from .models import Certificate
from .utils import sendTransaction
import hashlib
import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder






class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'nationality', 'subject', 'certificate_score', 'achievement_date')
    list_filter = ('subject', 'certificate_score')
    search_fields = ("surname__startswith",)
    readonly_fields = ('hash', 'txId')

    # overriding admin save method. Press save on admin panel to generate json hash and send transaction

    def save_model(self, request, obj, form, change):
        dict_for_json = model_to_dict(obj, fields={'name', 'surname', 'nationality', 'birth_date', 'subject',
                                                   'certificate_score',
                                                   'achievement_date', 'issuance_date'})
        json_for_hash = json.dumps(dict_for_json, sort_keys=True, indent=4, cls=DjangoJSONEncoder)

        obj.hash = hashlib.sha256(json_for_hash.encode('utf-8')).hexdigest()
        obj.txId = sendTransaction(obj.hash)

        super().save_model(request, obj, form, change)


admin.site.register(Certificate, CertificateAdmin)