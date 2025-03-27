from collections import namedtuple

Characteristic = namedtuple("Characteristic", [
    "name", "short_name", "rating_name", "initial_points", "added_points", "sum"])
Skill = namedtuple("Skill", [
    "name", "char_short_name", "char_sum", "added_points", "sum"])

characteristics = []
with open("characteristics.csv", "r") as f:
    characteristics = [Characteristic(*(x.strip() for x in l.split(", ") if x.strip() != ""))
              for l in f.readlines()]
characteristics = [Characteristic(c.name, c.short_name, c.rating_name, c.initial_points, c.added_points, str(int(c.added_points) + int(c.initial_points))) for c in characteristics]

def formatChar(char: Characteristic) -> str:
    return f'{char.name + ", ":16}{char.short_name + ", ":7}{char.rating_name + ", ":8}{char.initial_points + ", ":5}{char.added_points + ", ":5}{char.sum}\n'

with open("characteristics.csv", "w") as f:
    f.writelines((formatChar(c) for c in characteristics))
characteristics = {v.short_name: v.sum for _, v in enumerate(characteristics)}

skills = []
with open("skills.csv", "r") as f:
    skills = [Skill(*(x.strip() for x in l.split(", ") if x.strip() != ""))
              for l in f.readlines()]

skills = [Skill(s.name, s.char_short_name, characteristics[s.char_short_name], s.added_points, str(int(characteristics[s.char_short_name]) + int(s.added_points))) for s in skills]

def formatSkill(s: Skill) -> str:
    return f'{s.name + ", ":32}{s.char_short_name + ", ":8}{s.char_sum + ", ":5}{s.added_points + ", ":5}{s.sum}\n'

with open("skills.csv", "w") as f:
    f.writelines((formatSkill(s) for s in skills))
