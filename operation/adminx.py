import xadmin
from .models import Comments,UserFavorite,UserMessage
from account.models import UserProfile

class CommentsAdmin(object):
	list_display = ['user','add_time','comments']
	search_fields = ['user','add_time','comments']
	list_filter = ['user','add_time','comments']


class UserFavoriteAdmin(object):
	list_display = ['user','fav_id','fav_type','add_time']
	search_fields = ['user','fav_id','fav_type','add_time']
	list_filter = ['user','fav_id','fav_type','add_time']
	


class UserMessageAdmin(object):

	list_display = ['user','message','has_read','add_time']
	search_fields = ['user','message','has_read','add_time']
	list_filter = ['user','message','has_read','add_time']
	style_fields = {"message":"ueditor"}


xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(Comments,CommentsAdmin)
