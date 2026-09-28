import re

names = [" ana silva", "BRUNO COSTA", "carla Nunes "]

normalized_names = []

for name in names:
    name = re.sub(r"\s+", " ", name.strip())
    name = name.title()
    normalized_names.append(name)

print(normalized_names)