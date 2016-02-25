
from MonsterAttribute import MonsterAttribute
from MonsterAI import MonsterAI
from MonsterMovement import MonsterMovement
from MonsterSkill import MonsterSkill
from MonsterAction import MonsterAction
from MonsterAbnormality import MonsterAbnormality

class Monster:
    def __init__(self, area_id):
        self.area_id = area_id
        self.attr = MonsterAttribute(self)
        self.ai = MonsterAttribute(self)
        self.move = MonsterMovement(self)
        self.skill = MonsterSkill(self)
        self.action = MonsterAction(self)
        self.abnormality = MonsterAbnormality(self)

    def run(self, delta_time):
        self.attr.run(delta_time)
        self.ai.run(delta_time)
        self.move.run(delta_time)
        self.skill.run(delta_time)
        self.action.run(delta_time)
        self.abnormality.run(delta_time)

