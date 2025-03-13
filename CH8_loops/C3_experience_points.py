"""
Level	XP To Next Level	Total XP Gained
1	5	0
2	10	5
3	15	15
4	20	30

Complete the calculate_experience_points function.

The calculate_experience_points function takes a single parameter named level. 
Determine the total XP they have gained to reach the specified level from level 1 and return it.

"""

def calculate_experience_points(level):
    levelxp = 5
    totalxp = 0 
    for i in range(1,level):
        xp = i * levelxp
        totalxp += xp
    return totalxp
        