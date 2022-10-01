from django.contrib import admin
#형석 
from articles.models import Posts, Comments, PostImages, Bookmarks, Likes


# Register your models here.



#다솔

admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(PostImages)
admin.site.register(Bookmarks)
admin.site.register(Likes)
