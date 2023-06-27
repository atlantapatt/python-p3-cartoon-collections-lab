def roll_call_dwarves(names):
    i = 1
    for name in names:
        print(f"{i}. {name}")
        i += 1

def summon_captain_planet(calls):
    capitalized_calls = [f"{call.capitalize()}!" for call in calls ]
    return capitalized_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False
    
        

def find_the_cheese(lists):
    cheeses = ["cheddar", "gouda", "camembert"]
    find_cheese = [x for x in lists if any(lists in x for lists in cheeses)]
    if find_cheese == []:
        find_cheese = None
    else:
        find_cheese = ''.join(find_cheese)
    return find_cheese
    
