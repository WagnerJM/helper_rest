from uuid import UUID

from datetime import datetime

from app.api.user.models import User

def str2uuid(string):
    return UUID(string)

class ResourceMixin(object):
