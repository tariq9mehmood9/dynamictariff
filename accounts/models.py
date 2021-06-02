# from django.db import models
# from django.contrib.auth.models import User

# class tblUser(models.Model):
#     user = models.ForeignKey(User,default=None,to_field='username', on_delete=models.CASCADE)
#     userType = models.CharField(max_length=50)
#     atBus = models.CharField(max_length=50, default='1')
#     currActiveLoad = models.FloatField(default=0)
#     currReactiveLoad = models.FloatField(default=0)
#     consumedUnits = models.FloatField(default=0)
#     bill = models.FloatField(default=0)
#     image = models.ImageField(null=True, blank=True)
#     lastTime = models.CharField(max_length=20, default='01:00:00')
#     class Meta:
#         db_table = "tbl_users"

#     def __str__(self):
#         return self.user