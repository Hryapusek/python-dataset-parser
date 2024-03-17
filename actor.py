import json

class Actor:
    def __init__(self) -> None:
        self.actor_name = ""
        self.roles = []

    def to_postgres_format(self) -> str:
        res_str = ''
        res_str += '"' + self.actor_name + '",'
        roles_dict = {}
        roles_dict['roles'] = [role.to_dict() for role in self.roles]
        res_str += json.dumps(roles_dict)
        return res_str