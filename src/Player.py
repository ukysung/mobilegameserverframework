
from PlayerAttribute import PlayerAttribute
from PlayerMovement import PlayerMovement
from PlayerSkill import PlayerSkill
from PlayerAction import PlayerAction
from PlayerAbnormality import PlayerAbnormality

class Player:
    def __init__(self, area_id):
        self.area_id = area_id
        #self.attr = PlayerAttribute(self)
        self.move = PlayerMovement(self)
        self.skill = PlayerSkill(self)
        self.action = PlayerAction(self)
        self.abnormality = PlayerAbnormality(self)

    def run(self, delta_time):
        #self.attr.run(delta_time)
        self.move.run(delta_time)
        self.skill.run(delta_time)
        self.action.run(delta_time)
        self.abnormality.run(delta_time)

