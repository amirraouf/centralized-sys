import threading
import logging
from rest_framework.response import Response
from timeit import default_timer
logger = logging.getLogger(__name__)
LOCK = threading.Lock()


def lock(method):
    def wrapper(*args, **kwargs):
        start = default_timer()
        LOCK.acquire(blocking=True, timeout=3)
        while default_timer() - start < 15:
            try:
                return method(*args, **kwargs)
            finally:
                LOCK.release()
        return Response({'RunTimeError':'Your request exceed 15 seconds'})
    return wrapper
