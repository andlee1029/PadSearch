import os
import json


FILE_NAME = 'skill_api.json'

class RawSkill():
    def __init__(self, id, data):
        self.id: int = id
        self.name: str = data[0]
        self.text: str = data[1]

        # type may mean need to parse other fields
        self.skill_type: int = data[2]

        self.max_level: int = data[3] if data[3] != 0 else -1
        self.max_cooldown: int = data[4] if self.max_level != -1 else -1
        self.unknown1: str = data[5]
        self.remaining_data: list[str | int] = data[6:] 

    def get_skill_info(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.text
        }
   
    
    def __str__(self):
        return '''
            ID: {}\n
            Name: {}\n
            Description: {}\n
        '''.format(self.id, self.name, self.text)


def load_skill_data(directory = 'raw-data/', file_name = FILE_NAME) -> list[RawSkill]:
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    skills = [RawSkill(ind, s) for (ind,s) in enumerate(data['skill'])]
    return skills