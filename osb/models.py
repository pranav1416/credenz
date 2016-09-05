from django.db import models
from django.contrib.auth.models import User
import django

# event_flag = 1 then clash otherwise rc
#time_slot 1 to 20
#date_slot =  9 or 10



class Slot(models.Model):
    room_no = models.CharField(max_length = 5,blank = False)
    total_comp = models.IntegerField(blank = False)
    comp_avail = models.IntegerField(blank = False)
    date_slot = models.IntegerField(blank = False)
    time_slot = models.IntegerField(blank = False)
    event_flag = models.BooleanField(blank = False)
    def __str__(self):
        return (self.room_no)
        

class UserData(models.Model):
    registration_id = models.IntegerField(blank = False)
    name1 = models.CharField(max_length=30,null=True)
    name2 = models.CharField(max_length=30,blank=True,null = True)  
    email1 = models.EmailField(null = True)
    email2 = models.EmailField(null = True)
    mobile_no1 = models.CharField(max_length = 10,null = True)
    mobile_no2 = models.CharField(max_length = 10,blank = True,null = True)
    event_flag = models.BooleanField(blank = False)
    password = models.CharField(max_length = 6)     #Randomly generated and assigned by a function and same password will be used in User    
    slot_booked = models.BooleanField(default = False)             #if 1 cannot login again   
    send_mail = models.BooleanField(default = False)        #set to 1 when the mail is sent
    user = models.OneToOneField(User)
    slot = models.ForeignKey(Slot,blank = True)
    def __str__(self):
        return (self.name1)

class ExcelData(models.Model):
    user_id = models.IntegerField(default = 2046)
    def __str__(self):
        return (self.user_id)        
#college name and class of the participant is not stored
