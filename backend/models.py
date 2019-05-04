from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(User):
    event_id = models.ForeignKey("Event", on_delete=models.PROTECT, null=False, blank=False)

class Runner(models.Model):
    bib = models.IntegerField(primary_key=True)
    SIZE = (
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
    )
    size = models.CharField(choices=SIZE,max_length=2)
    runner_firstname = models.CharField(max_length=50)
    runner_lastname = models.CharField(max_length=50)
    regist_id =  models.ForeignKey("RegisterInfo",on_delete=models.PROTECT)
    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    sex = models.CharField(choices=SEX, max_length=50)
    def __str__(self):
        return str(self.bib) + " "+ self.runner_firstname+ " "+ self.runner_lastname+ " " + self.sex


class Driver(models.Model):
    driver_id = models.IntegerField(primary_key=True)
    d_firstname = models.CharField(max_length=50)
    d_lastname = models.CharField(max_length=50)
    d_phone = models.CharField(max_length=10)
    team_id = models.ForeignKey("Team", on_delete=models.PROTECT, null=False, blank=False)
    def __str__(self):
        return self.driver_id + " "+ self.d_firstname+" "+self.d_lastname+" "+self.d_phone

class Manager(models.Model):
    manager_id = models.IntegerField(primary_key = True)
    m_firstname = models.CharField(max_length=50)
    m_lastname = models.CharField(max_length=50)
    m_phone = models.CharField(max_length=10)
    m_email = models.EmailField(max_length=254)
    team_id = models.ForeignKey("Team", on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return "%d %s %s %s %s" % (self.manager_id, self.m_firstname, self.m_lastname, self.m_phone)

class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=50)
    e_date = models.DateField(auto_now=False, auto_now_add=False)
    e_locations = models.TextField()

    def __str__(self):
        return "%d %s %s" % (self.event_id, self.event_name, self.e_date)

class CheckPoint(models.Model):
    checkpoint_no = models.IntegerField(primary_key =True)
    round_no = models.IntegerField()
    lap_distant = models.FloatField()
    place = models.CharField(max_length=50)
    total_distant = models.FloatField()

    def __str__(self):
        return "%d %s" % (self.checkpoint_no, self.checkpoint_name)

class RunningType(models.Model):
    running_type_id = models.IntegerField(primary_key=True)
    catergory = models.CharField(max_length=255)
    def __str__(self):
        return "%d %s" % (self.running_type_id, self.catergory)

class Team(Runner):
    team_id = models.IntegerField()
    team_name = models.CharField (max_length=100)
    resident = models.BooleanField()
    TEAM_TYPE = (
        ('team_need_runner', 'Team Need Runner'),
        ('runner_need_team', 'Runner Need Team'),
    )
    team_type = models.CharField(choices=TEAM_TYPE, max_length=50)
    def __str__(self):
        return "%d %s" % (self.team_id, self.team_name)

class SoloRunner(Runner):
    solo_runner_id= models.IntegerField()
    bus = models.BooleanField()
    resident = models.BooleanField()
    def __str__(self):
        return "%d" % (self.solo_runner_id)

class RegisterInfo(models.Model):
    regist_id = models.IntegerField(primary_key=True)
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    pay_inSlip = models.CharField(max_length=255)
    event_id = models.ForeignKey(
        "Event", on_delete=models.PROTECT, null=False, blank=False)
    running_type_id = models.ForeignKey("RunningType", on_delete=models.PROTECT, null=False, blank=False)
    def __str__(self):
        return "%d" % (self.regist_id)
    

class Certificate(models.Model):
    cer_id = models.IntegerField(primary_key=True)
    cer_url = models.CharField(max_length=255)
    runner_bib = models.ForeignKey("Runner", on_delete=models.CASCADE)


class Runner_Checkpoint(models.Model):
    runner_bib = models.ForeignKey("Runner", on_delete=models.CASCADE)
    checkpoint_no = models.ForeignKey(
        "CheckPoint", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    #surrogate keys
    class Meta:
        unique_together = (('runner_bib', 'checkpoint_no'),)

    def __str__(self):
        return "%d %d" % (self.runner_bib, self.checkpoint_no)

class News(models.Model):
    news_id = models.IntegerField(primary_key=True)
    eng_content = models.TextField()
    thai_content = models.TextField()
    event_id = models.ForeignKey("Event", on_delete=models.PROTECT, null=False, blank=False)
    def __str__(self):
        return "%d" % (self.news_id)
