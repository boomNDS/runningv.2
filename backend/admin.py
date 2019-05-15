from django.contrib import admin
from .models import *

# Register your models here.

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'regist_id', 'checkpoint_no', 'start_time','end_time']
    list_per_page = 10

    list_filter = ['regist_id', 'checkpoint_no']
    search_fields = ['regist_id', 'checkpoint_no']
admin.site.register(competition_results,CompetitionAdmin)
class CheckPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'round_no', 'lap_distant', 'place','total_distant']
    list_per_page = 10

    list_filter = ['round_no','place']
    search_fields = ['round_no','place']
admin.site.register(CheckPoint,CheckPointAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'e_locations']
    list_per_page = 10

    list_filter = ['e_locations']
    search_fields = ['event_name']
admin.site.register(Event,EventAdmin)

class RunnerAdmin(admin.ModelAdmin):
    list_display = ['id','team_id', 'regist_id', 'runner_firstname','runner_lastname','size']
    list_per_page = 10
    list_filter = ['regist_id','team_id']
    search_fields = ['regist_id','team_id']
admin.site.register(Runner,RunnerAdmin)

class RunningTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'catergory']
    list_per_page = 10
    list_filter = ['catergory']
    search_fields = ['catergory']
admin.site.register(RunningType,RunningTypeAdmin)

class SoloRunnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'bus','resident','runner_bib']
    list_per_page = 10
    # list_filter = ['catergory']
    # search_fields = ['catergory']
admin.site.register(SoloRunner,SoloRunnerAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_email', 'payment_date', 'running_type_id']
    list_per_page = 10

    list_filter = ['running_type_id']
    search_fields = ['user_email']

    # Add another model (need to create class)
admin.site.register(RegisterInfo,RegisterAdmin)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'cer_url', 'runner_bib']
    list_per_page = 10
    search_fields = ['runner_bib']
admin.site.register(Certificate,CertificateAdmin)

class Runner_CheckpointAdmin(admin.ModelAdmin):
    list_display = ['id', 'runner_bib', 'checkpoint_no','time']
    list_per_page = 10
    list_filter = ['checkpoint_no']
    search_fields = ['runner_bib','checkpoint_no']
admin.site.register(Runner_Checkpoint,Runner_CheckpointAdmin)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'team_id', 'm_firstname','m_lastname','m_phone','m_email']
    list_per_page = 10
    search_fields = ['team_id','m_firstname','m_lastname','m_email']
admin.site.register(Manager,ManagerAdmin)

class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'team_id', 'd_firstname','d_lastname','d_phone']
    list_per_page = 10
    search_fields = ['team_id','d_firstname','d_lastname','d_phone']
admin.site.register(Driver,DriverAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','event_id', 'eng_content', 'thai_content']
    list_per_page = 10
    search_fields = ['event_id']
admin.site.register(News,NewsAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','team_name', 'resident', 'team_type']
    list_per_page = 10
    list_filter = ['team_type','resident']
    search_fields = ['team_name']
admin.site.register(Team,TeamAdmin)

