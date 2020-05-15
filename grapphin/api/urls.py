"""
REST urls.
"""

from api.routers import GraphRouter
from mind import viewsets as mind
# from users import viewsets as users


router = GraphRouter(trailing_slash=False)
router.include(mind.GTreeView)
router.include(mind.GNodeView)
router.include(mind.GContentView)
# router.include(users.User)

urlpatterns = router.urls
