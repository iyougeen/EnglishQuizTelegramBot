from django.shortcuts import render
from .models import Word, Player, Poll


# Create your views here.
def index(request):
    words_cnt = Word.objects.count()
    players_cnt = Player.objects.count()
    top_five_players = Player.objects.order_by("-num_right_answers")[:5]
    context = {"words_cnt": words_cnt, "players_cnt": players_cnt, "top_five_players": top_five_players}
    return render(request, "bot/index.html", context)
