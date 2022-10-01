from django.db import models

# Create your models here.


#웅주 형석 Posts
class Posts(models.Model):
    user_id = models.IntegerField(default=0) # FK    
    content = models.TextField(max_length=256) #포스트 내용 - 최대 256
    modified_at = models.DateTimeField(auto_now=True) # 포스팅 수정 시간
    created_at = models.DateTimeField(auto_now_add=True) #포스팅 생성 시간
    bio = models.CharField(max_length=256, blank=True) # 자기소개 

# 남훈 comments
class Comments(models.Model):
    post_id = models.IntegerField(default=0) # post id
    user_id = models.IntegerField(default=0) # user id
    content = models.TextField() # 코멘트 내용
    created_at = models.DateTimeField(auto_now_add=True) # 코멘트 생성 시간
    modified_at = models.DateTimeField(auto_now=True) # 코멘트 수정 시간

# 다솔 Post_images
class PostImages(models.Model):
    post_id = models.IntegerField(default=0) # post id
    post_image = models.TextField(max_length=256, blank=True) # 포스트 이미지

# 은혜 Booksmarks
class Bookmarks(models.Model):
    user_id = models.IntegerField(default=0)
    post_id = models.IntegerField(default=0)
    
# likes
class Likes(models.Model):
    post_id = models.IntegerField(default=0) # 포스트 id
    user_id = models.IntegerField(default=0) # 유저 id



