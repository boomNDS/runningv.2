from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Runner(models.Model):
    SIZE = (
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
    )
    size = models.CharField(choices=SIZE,max_length=3)
    runner_firstname = models.CharField(max_length=50)
    runner_lastname = models.CharField(max_length=50)
    regist_id =  models.ForeignKey("RegisterInfo",on_delete=models.PROTECT, null=False)
    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    sex = models.CharField(choices=SEX, max_length=50)
    team_id = models.ForeignKey(
        "Team", on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.runner_firstname+ " "+ self.runner_lastname+ " " + self.sex


class Driver(models.Model):
    d_firstname = models.CharField(max_length=50)
    d_lastname = models.CharField(max_length=50)
    d_phone = models.CharField(max_length=10)
    team_id = models.OneToOneField("Team", on_delete=models.PROTECT, null=False, blank=False)
    def __str__(self):
        return self.d_firstname+" "+self.d_lastname+" "+self.d_phone

class Manager(models.Model):
    m_firstname = models.CharField(max_length=50)
    m_lastname = models.CharField(max_length=50)
    m_phone = models.CharField(max_length=10)
    m_email = models.EmailField(max_length=254)
    team_id = models.OneToOneField("Team", on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return "%s %s %s %s" % (self.m_firstname, self.m_lastname, self.m_phone)

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    e_date = models.DateField(auto_now=False, auto_now_add=False)
    e_locations = models.TextField()

    def __str__(self):
        return "%s %s" % (self.event_name, self.e_date)

class CheckPoint(models.Model):
    round_no = models.IntegerField()
    lap_distant = models.FloatField()
    place = models.CharField(max_length=50)
    total_distant = models.FloatField()

    def __str__(self):
        return "%s" % (self.place)

class RunningType(models.Model):
    CATERGORY = (
        ('open junior', ' ประเภทจูเนียร์ทั่วไป อายุรวมกันไม่เกิน 280 ปี'),
        ('mixed junior', 'ประเภทจูเนียร์ผสม อายุรวมกันไม่เกิน 260 ปี'),
        ('open super junior', 'ประเภทซุปเปอร์จูเนียร์ทั่วไป อายุรวมกันตั้งแต่ 281 – 360'),
        ('mixed super junior', 'ประเภทซุปเปอร์จูเนียร์ผสม อายุรวมกันตั้งแต่ 261 – 340 ปี'),
        ('open senior ', 'ประเภทซีเนียร์ทั่วไป อายุรวมกันตั้งแต่ 361 – 440 ปี'),
        ('mixed senior ', 'ประเภทฃีเนียร์ผสม อายุรวมกันตั้งแต่ 341 – 420 ปี'),
        ('open super senior', 'ประเภทซูเปอร์ซีเนียร์ทั่วไป อายุรวมกันตั้งแต่ 441 ปีขึ้นไป'),
        ('mixed super senior ', 'ประเภทซูปซีเนียร์ผสม อายุรวมกันตั้งแต่ 421 ปีขึ้นไป'),
        ('open female', 'ประเภทหญิงทั่วไป ไม่จำกัดอายุ'),
        ('solo runner', 'ประเภทเดี่ยว ระยะ 120 km.'),
    )
    catergory = models.CharField(choices=CATERGORY, max_length=255)
    def __str__(self):
        return "%s" % (self.catergory)

class Team(Runner):
    team_name = models.CharField (max_length=100)
    resident = models.BooleanField()
    TEAM_TYPE = (
        ('team need runner', 'Team Need Runner'),
        ('runner need team', 'Runner Need Team'),
    )
    team_type = models.CharField(choices=TEAM_TYPE, max_length=50)
    def __str__(self):
        return "%s" % (self.team_name)

class SoloRunner(models.Model):
    bus = models.BooleanField()
    resident = models.BooleanField()
    runner_bib = models.ForeignKey("Runner", on_delete=models.PROTECT , null = False)
    
class RegisterInfo(models.Model):
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    pay_inSlip = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    event_id = models.ForeignKey(
        "Event", on_delete=models.PROTECT, null=False, blank=False)
    running_type_id = models.ForeignKey("RunningType", on_delete=models.PROTECT, null=False, blank=False)
    user_email = models.EmailField(max_length=254)
    def __str__(self):
        return "%s" % (self.user_email)
    

class Certificate(models.Model):
    cer_url = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)
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
    eng_content = models.TextField()
    thai_content = models.TextField()
    event_id = models.ForeignKey("Event", on_delete=models.PROTECT, null=False, blank=False)
