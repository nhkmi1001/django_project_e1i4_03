from django.db import models
# Create your models here.

# 은혜

class UserModel(models.Model):
    
    password = models.CharField(max_length=256, null=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True) # 코멘트 생성 시간
    last_login = models.TextField()
    modified_at = models.DateTimeField(auto_now=True) # 코멘트 수정 시간
    

#웅주

class Follows(models.Model):
    user_id = models.IntegerField(default=0)    # 유저 id
    follow_user_nickname = models.IntegerField(default=0) #(보류)
    
