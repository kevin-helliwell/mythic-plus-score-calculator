import requests
import json

def time_bonus_calculator(par_time, completion_time):
    if completion_time>par_time:
        return
    elif completion_time==par_time:
        return 0
    elif completion_time<=0.6*par_time:
        return 7.5
    else:
        x1, y1 = par_time, 0
        x2, y2 = 0.6*par_time, 7.5
        slope = (y2-y1)/(x2-x1)
        score = slope*completion_time + 18.75
        return score
        
# print(time_bonus_calculator(1000,1400))
# print(time_bonus_calculator(1000,1000))
# print(time_bonus_calculator(1000,600))
# print(time_bonus_calculator(1000,500))
# print(time_bonus_calculator(1000,800))

# Character info
location = "us"
server = "Zul'Jin"
toon_name = "konnenh"
total_num_dungeons = 10

best_runs = requests.get(f"https://raider.io/api/v1/characters/profile?region={location}&realm={server}&name={toon_name}&fields=mythic_plus_best_runs")
best_runs_data = best_runs.text
best_runs_parsed_json = json.loads(best_runs_data)
best_scores = []
best_dungeons = []

best_alt_runs = requests.get(f"https://raider.io/api/v1/characters/profile?region={location}&realm={server}&name={toon_name}&fields=mythic_plus_alternate_runs")
best_alt_runs_data = best_alt_runs.text
best_alt_runs_parsed_json = json.loads(best_alt_runs_data)
best_alt_scores = []
best_alt_dungeons = []

# Appends necessary info for score calculation
for i in range(total_num_dungeons):

    best_score = best_runs_parsed_json["mythic_plus_best_runs"][i]["score"]
    best_scores.append(best_score)
    
    best_dungeon = best_runs_parsed_json["mythic_plus_best_runs"][i]["short_name"]
    best_dungeons.append(best_dungeon)
    
    alt_score = best_alt_runs_parsed_json["mythic_plus_alternate_runs"][i]["score"]
    best_alt_scores.append(alt_score)
    
    alt_dungeon = best_alt_runs_parsed_json["mythic_plus_alternate_runs"][i]["short_name"]
    best_alt_dungeons.append(alt_dungeon)

best_dict = dict(zip(best_dungeons, best_scores))
alt_dict = dict(zip(best_alt_dungeons, best_alt_scores))

print(best_dict)
print(alt_dict)
total_score = 0

for i in range(len(best_dungeons)):
    dungeon = f"{best_dungeons[i]}"
    print(dungeon)
    best_score = best_dict.get(dungeon)
    print(best_score)
    alt_score = alt_dict.get(dungeon)
    print(alt_score)
    total_score+=best_score+alt_score

print(total_score)

