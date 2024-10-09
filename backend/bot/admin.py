from django.contrib import admin
from .models import Word, Player, Poll


# Register your models here.
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'translate', 'last_picked')
    ordering = ['-last_picked']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'num_right_answers', 'num_wrong_answers')
    ordering = ['-num_right_answers']


class PollAdmin(admin.ModelAdmin):
    list_display = ('poll_id', 'poll_question', 'poll_right_asnwer', 'date_create')
    ordering = ['-date_create']


admin.site.register(Word, WordAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Poll, PollAdmin)
