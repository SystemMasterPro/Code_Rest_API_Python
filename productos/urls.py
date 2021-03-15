from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('', ProductoViewset)
router.register('api/almacenes',AlmacenViewset)

urlpatterns = router.urls