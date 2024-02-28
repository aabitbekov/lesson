import datetime
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.models import LogEntry  
from django.contrib import messages
from rangefilter.filters import DateRangeFilter
from .models import Signal, Incident
from .elastic_client_dev import getLast30Coincidence, getSignalsFromCoincidenceHits, getCoincidences
from .readHits import readSignalsHits, readIncidentHits
from django.db.models import Q


class CustomDateTimeRange(DateRangeFilter):
    def queryset(self, request, queryset):
        start_date_str = request.GET.get('timestamp__range__gte')
        end_date_str = request.GET.get('timestamp__range__lte')
        # q = request.GET.get('q')
        if start_date_str == None and end_date_str == None:
            super().queryset(request, queryset)
        else:
            hits, err = getCoincidences(start_date_str, end_date_str)
            if err == None:
                signalHits, err = getSignalsFromCoincidenceHits(hits=hits)
                if err == None:
                    signal_objects = readSignalsHits(signalHits)
                    Signal.objects.all().delete()
                    Signal.objects.bulk_create(signal_objects)
                else:
                    messages.error(request, f"Ошибка подключение к elastic/qainar-signals/: {err}")
                    # raise ValidationError(f"Ошибка подключение к elastic/qainar-signals/: {err}")
            else:
                messages.error(request, f"Ошибка подключение к elastic/qainar-signals/: {err}")
                # raise ValidationError(f"Ошибка подключение к elastic/qainar-coincidence/: {err}")    

            return readIncidentHits(hits)  


class IPFilter(admin.SimpleListFilter):
    title = _('IP')  
    parameter_name = 'IP'  

    def lookups(self, request, model_admin): 
        return (
            ('dst', _('DST')),
            ('src', _('SRC')),
        )
  
    def queryset(self, request, queryset):
        if self.value() == 'dst':
            return queryset.filter(ip_dst__isnull=False)
        elif self.value() == 'src':
            return queryset.filter(ip_src__isnull=False)


class SignalAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip_src', 'ip_dst', 'user', 'uid')
    list_filter = (IPFilter, )
    search_fields = ('id', 'ip_src', 'ip_dst')


class SignalInline(admin.TabularInline):  # или StackedInline
    model = Incident.signals.through
    extra = 1


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip', 'matching_count'
                    , 'display_signals')
    search_fields = ['id', 'ip', 'signals__ip_src', 'signals__ip_dst', 'timestamp']
    list_filter = (
        ('timestamp', CustomDateTimeRange),
        )
    exclude = ('signals',)
    inlines = [SignalInline]
    

    def get_queryset(self, request):
        hits, err = getLast30Coincidence()
        if err == None:
            signalHits, err = getSignalsFromCoincidenceHits(hits=hits)
            if err == None:
                signal_objects = readSignalsHits(signalHits)
                Signal.objects.all().delete()
                Signal.objects.bulk_create(signal_objects)
            else:
                raise ValidationError(f"Ошибка подключение к elastic/qainar-signals/: {err}")
        else:
            raise ValidationError(f"Ошибка подключение к elastic/qainar-coincidence/: {err}")    
        return readIncidentHits(hits)   
    
    def get_search_results(self, request, queryset, search_term):
        # Разбиваем введенные пользователем значения по запятой и удаляем лишние пробелы
        search_terms = [term.strip() for term in search_term.split(',') if term.strip()]

        # Создаем объект Q для каждого значения и объединяем их оператором ИЛИ
        query = Q()
        for term in search_terms:
            for field in self.search_fields:
                query |= Q(**{f'{field}__icontains': term})

        # Фильтруем queryset по созданным Q объектам
        queryset = queryset.filter(query).distinct()

        return queryset, False
    
    def display_signals(self, obj):
        return mark_safe("<br>".join([related.link_to_object() for related in obj.signals.all()]))
    
    def get_rangefilter_timestamp_default(self, request):
        return (datetime.date.today, datetime.date.today)
    
    display_signals.short_description = 'Сигналы'


admin.site.register(Incident, IncidentAdmin)
admin.site.register(Signal, SignalAdmin)
admin.site.register(LogEntry)