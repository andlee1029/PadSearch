from django.shortcuts import render
from django.http import HttpResponse
from .models import Monster, MonsterType, MonsterAttribute, Skill
from .forms import MonsterSearchForm
from .utils import get_monster_image, print_monster

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        # use form to get query parameters
        form = MonsterSearchForm(request.POST)
        monster_objects = Monster.objects.all()
        
        if form.is_valid():
            if form.cleaned_data['evolutions'] is not None:
                monster_objects = monster_objects.filter(owned=int(not form.cleaned_data['evolutions']))
            if form.cleaned_data['monster_name'] is not None:
                monster_objects = monster_objects.filter(monster_name__icontains=form.cleaned_data['monster_name'])
            if form.cleaned_data['monster_num'] is not None:
                monster_objects = monster_objects.filter(monster_id__exact=form.cleaned_data['monster_num'])
            if form.cleaned_data['monster_types'] is not None and len(form.cleaned_data['monster_types']) > 0:
                monster_objects = monster_objects.filter(monster_types={'monster_type':int(form.cleaned_data['monster_types'][0])})
            if form.cleaned_data['monster_attributes'] is not None and len(form.cleaned_data['monster_attributes']) > 0:
                monster_objects = monster_objects.filter(monster_attributes={'monster_attribute':int(form.cleaned_data['monster_attributes'][0])})
        
    else:
        # initially jsut show all owned monsters
        monster_objects = Monster.objects.all()
        monster_objects = monster_objects.filter(owned=True)
        form = MonsterSearchForm().as_ul()

    monsters = []
    for monster in monster_objects:
        monster_dict = {
            "id": monster.monster_id,
            "name": monster.monster_name,
            "awakenings": monster.monster_awakenings,
            "askill": monster.askill_id, #should later be updated with actual text
            "lskill": monster.lskill_id,
            "image_path": get_monster_image(monster.monster_id)
        }
        askill = Skill.objects.filter(id=monster_dict["askill"])[0]
        lskill = Skill.objects.filter(id=monster_dict["lskill"])[0]
        monster_dict["askill"] = askill.description
        monster_dict["lskill"] = lskill.description
        monsters.append(monster_dict)

    # testmon = Monster.objects.all()
    # print("starting test")
    # print(len(testmon))
    # testmon = testmon.filter(owned=0)
    # print(len(testmon))
    context["form"] = form
    context["monsters"] = monsters
    return render(request, "monstersearch/request.html", context)