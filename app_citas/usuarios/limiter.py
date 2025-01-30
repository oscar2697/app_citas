from django.core.cache import cache
from django.http import HttpResponse
import time


def rate_limit(requests_per_minute=60):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            # Crea una key única por IP
            ip = request.META.get("REMOTE_ADDR")
            key = f"rate_limit_{ip}"

            # Obtiene el contador actual
            requests = cache.get(key, {"count": 0, "reset_time": time.time()})

            # Verifica si necesitamos resetear el contador
            if time.time() - requests["reset_time"] >= 60:
                requests = {"count": 0, "reset_time": time.time()}

            # Incrementa el contador
            requests["count"] += 1

            # Si excede el límite, retorna error
            if requests["count"] > requests_per_minute:
                return HttpResponse("Rate limit exceeded", status=429)

            # Guarda el nuevo contador
            cache.set(key, requests, timeout=60)

            return func(request, *args, **kwargs)

        return wrapper

    return decorator
