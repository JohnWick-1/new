from .views import *


from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'student', StudentViewSet)
# router.register(r'student2', Student2View)
print('inside app level urls')
urlpatterns = router.urls
