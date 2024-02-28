from .models import Signal, Incident

def readSignalsHits(hits):
    signal_objects = []
    for hit in hits:
        id = hit.get("_id")
        source = hit.get("_source", {})
        event = source.get("event", {})
        timestamp = event.get("timestamp")
        ip_src = event.get("ip_src", [])
        ip_dst = event.get("ip_dst", [])
        identifiers = source.get("identifiers", {})
        uid = identifiers.get('uid')
        user = identifiers.get('user')
        if ip_src is not None and ip_dst is not None:
            ip_src, ip_dst = ip_src[0], ip_dst[0]
        elif ip_dst is None and ip_src is not None:
            ip_src = ip_src[0]
        elif ip_src is None and ip_dst is not None:
            ip_dst = ip_dst[0]
        signal_objects.append(Signal(id=id, timestamp=timestamp, ip_src=ip_src, ip_dst=ip_dst, uid=uid, user=user)) 
    return signal_objects


def readIncidentHits(hits):
    Incident.objects.all().delete()
    for hit in hits:
        id = hit.get("_id")
        source = hit.get("_source", {})
        timestamp = source.get("@timestamp")
        signals = source.get("signal_id", [])
        ip = source.get("ip")
        matching_count = source.get("matching_count")
        incident = Incident(id=id, timestamp=timestamp, ip=ip, matching_count=matching_count)
        incident.save()
        incident.signals.set(Signal.objects.filter(id__in=signals))
        incident.save()
    return Incident.objects.all()
