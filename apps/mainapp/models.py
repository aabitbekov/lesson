# YourApp/models.py
from django.db import models
from django.urls import reverse
from django.utils.html import format_html


def getBankByUid(uid):
    banks = {
        1243 : 'Kaspi Bank',
        1253 : 'Alhilal Bank',
        1260 : 'Zaman Bank',
        1261 : 'Nur Bank',
        1266 : 'Halyk Bank',
        1267 : 'VTB Bank',
        1269 : 'Bereke Bank',
        1276 : 'Citi Bank',
        1306 : 'QazSOC',
        1004 : 'AFR',                
        1233 : 'Altyn Bank',
        1235 : 'BCC',
        1238 : 'Jusan Bank',
        1239 : 'euBank',
        1240 : 'RBK Bank',
        1241 : 'Forte Bank',
        1242 : 'Shinhan Bank',
        1246 : 'hcsbk',
        1247 : 'boc',
        1248 : 'homecredit',
        1252 : 'kzi Bank',
        1259 : 'BankFin',
        
    }
    return banks[uid]
class Signal(models.Model):

    id = models.CharField(max_length=128, primary_key=True)

    timestamp = models.DateTimeField(
        verbose_name="Дата и время",
        blank=False,
        null=False,
        )
    
    ip_src = models.GenericIPAddressField(
        verbose_name="SRC IP",
        blank=True,
        null=True
        )
    
    ip_dst = models.GenericIPAddressField(
        verbose_name="DST IP",
        blank=True, 
        null=True
        )
    
    uid = models.IntegerField(("id Источника"))

    user = models.IntegerField(("Источник"))

    class Meta:
        verbose_name = 'Сигнал'
        verbose_name_plural = 'Сигналы'


    def link_to_object(self):
        object_url = reverse('admin:mainapp_signal_change', args=[self.id])
        return format_html('<a href="{}">{}</a>', object_url, self.__str__())

    link_to_object.allow_tags = True  # For Django versions up to 1.11
    
    def __str__(self):
        bank = getBankByUid(self.user)
        if self.ip_dst:
            return f"*timestamp: {self.timestamp}   IP_SRC ⭕ : {self.ip_src}  IP_DST ❌ : {self.ip_dst}     {self.user}"
        
        else:
            return f"*timestamp: {self.timestamp}   IP_SRC ⭕ : {self.ip_src}    {bank}"

        
    

class Incident(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    timestamp = models.DateTimeField(
        verbose_name="Дата и время",
        blank=False,
        null=False
        )
    ip = models.GenericIPAddressField(
        verbose_name="IP-адрес",
        blank=True, 
        null=True   
        )
    matching_count = models.IntegerField(verbose_name="Сигналы")
    signals = models.ManyToManyField(Signal, verbose_name="Сигналы")


    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'


        