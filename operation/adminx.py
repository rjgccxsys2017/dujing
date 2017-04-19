import xadmin
from .models import Comments,UserFavorite,UserMessage
from account.models import UserProfile

class CommentsAdmin(object):
	pass
	
xadmin.site.register(Comments,CommentsAdmin)

class UserFavoriteAdmin(object):
	pass
	
xadmin.site.register(UserFavorite,UserFavoriteAdmin)

class UserMessageAdmin(object):
	pass
	
xadmin.site.register(UserMessage,UserMessageAdmin)