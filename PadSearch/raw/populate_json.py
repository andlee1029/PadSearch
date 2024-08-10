import json
from player_data import load_player_data
from monster import load_monster_data, RawMonster
from skill import load_skill_data, RawSkill

# write fixtures for owned monsters
owned_ids: set[int] = set(load_player_data('raw/raw-data/'))
monster_box_ids: set[int] = owned_ids.copy()
monsters: list[RawMonster] = load_monster_data('raw/raw-data/')

monster_box: list[RawMonster] = []
for mon in monsters:
    if (mon.id in monster_box_ids) or (mon.root_id in monster_box_ids):
        monster_box.append(mon)
        monster_box_ids.add(mon.root_id)

fixture_dicts = []

for mon in monster_box:
    fields = mon.get_monster_info()
    
    fields['owned'] = int(mon.id in owned_ids)

    if 'monster_types' in fields.keys():
        fields['monster_types'] = [{
            "monster_type":t
        } for t in fields['monster_types']]

    if 'monster_attributes' in fields.keys():
        fields['monster_attributes'] = [{
            "monster_attribute":t
        } for t in fields['monster_attributes']]
    if 'awakenings' in fields.keys():
        fields['awakenings'] = [{
            "awakening": t
        } for t in fields['awakenings']]
    if 'super_awakenings' in fields.keys():
        fields['super_awakenings'] = [{
            "awakening": t
        } for t in fields['super_awakenings']]

    fixture_dicts.append(fields)
print(fixture_dicts)


monsters_json = json.dumps(fixture_dicts)
with open('raw/raw-jsons/monsters.json','w') as f:
    f.write(monsters_json)


skills: list[RawSkill] = load_skill_data('raw/raw-data/')
skills_json = json.dumps([s.get_skill_info() for s in skills])
with open('raw/raw-jsons/skills.json','w') as f:
    f.write(skills_json)
