from djongo import models

# Create your models here.
class MonsterType(models.Model):
    class Type(models.IntegerChoices):
        EVO_MATERIAL = 0, "EVO_MATERIAL"
        BALANCED = 1, "BALANCED"
        PHYSICAL = 2, "PHYSICAL"
        HEALER = 3, "HEALER"
        DRAGON = 4, "DRAGON"
        GOD = 5, "GOD"
        ATTACKER = 6, "ATTACKER"
        DEVIL = 7, "DEVIL"
        MACHINE = 8, "MACHINE"
        AWAKEN_MATERIAL = 12, "AWAKEN_MATERIAL"
        ENHANCE_MATERIAL = 14, "ENHANCE_MATERIAL"
        REDEEMABLE_MATERIAL = 15, "REDEEMABLE_MATERIAL"
    monster_type = models.IntegerField(blank=False,choices=Type.choices)

    class Meta:
        abstract = True

class MonsterAttribute(models.Model):
    class Attribute(models.IntegerChoices):
        FIRE = 0, "FIRE"
        WATER = 1, "WATER"
        WOOD = 2, "WOOD"
        LIGHT = 3, "LIGHT"
        DARK = 4, "DARK"
        EMPTY = 6, "EMPTY"
    monster_attribute = models.IntegerField(blank=False,choices=Attribute.choices)

    class Meta: 
        abstract = True

class MonsterAwakening(models.Model):
    awakening = models.IntegerField(blank=False)

    class Meta:
        abstract = True

class Monster(models.Model):
    _id = models.ObjectIdField()
    owned = models.IntegerField() # currently just using integer field with values 0, 1 bc querying bool with djongo seems to fail
    monster_id = models.BigIntegerField()
    monster_name = models.CharField(max_length=100)
    askill_id = models.BigIntegerField()
    lskill_id = models.BigIntegerField()
    monster_types = models.ArrayField(model_container=MonsterType)
    monster_attributes = models.ArrayField(model_container=MonsterAttribute)
    monster_awakenings = models.ArrayField(model_container=MonsterAwakening)
    monster_super_awakenings = models.ArrayField(model_container=MonsterAwakening)
    root_id = models.BigIntegerField()


    objects = models.DjongoManager()

class Skill(models.Model):
    _id = models.ObjectIdField()
    id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()

    
    objects = models.DjongoManager()

