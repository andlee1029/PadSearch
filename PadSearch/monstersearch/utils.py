import json
from os.path import exists, join
import os
from .models import Monster, MonsterAttribute, MonsterType

def get_monster_image(id: int) -> str:
    image_file_name = 'monstersearch/static/monstersearch/monster_images/monster_pic'+ str(id) + '.PNG'
    if not exists(image_file_name): 
        # build image using image module
        print("get_monster_image: image not found so creating")
        print("get_monster_image: current path is ", os.getcwd())
        return ""
    return 'monstersearch/monster_images/monster_pic' + str(id) + '.PNG'




def print_monster(monster: Monster) -> str:
    askill = monster.askill_id_askill
    lskill = monster.lskill_id_lskill

    return json.dumps({
        "monster_id" : monster.monster_id,
        "monster_name" : monster.monster_name,
        "active_skill_name" : askill.askill_name,
        "active_skill_desc" : askill.askill_desc,
        "leader_skill_name" : lskill.lskill_name,
        "leader_skill_desc" : lskill.lskill_desc,
    })
