import time
import sys
from Import import *
from ActivityPlanGenerator import *

def generate_activity_plans(generator, number_of_plans):
    activity_plans = []
    for i in range(0, number_of_plans):
        activity_plans.append(generator.generate_random_activity_plan())
    return activity_plans

def random_variation(random_elite1, random_elite2):
    candidate = ActivityPlanGenerator.crossover(random_elite1, random_elite2)
    if random.random() < crossoverRate:
        candidate = generator.mutate(candidate)
    return candidate

def get_best_plans_total_score(plans, number_of_plans_to_get):
    sorted_plans = sorted(plans, key=lambda plan: plan.total_score, reverse=True)
    return sorted_plans[:int(number_of_plans_to_get)]

def add_if_new_or_better(dim, score, new_plan):
    if (score in dim):
        existing = dim[score]
        if new_plan.total_score <= existing.total_score: return
    dim[score] = new_plan

funAndSafeDim = {}
def add_to_funAndSafeDim(plan):
    add_if_new_or_better(funAndSafeDim, plan.fun_and_safe_score, plan)

highRiskHighRewardDim = {}
def add_to_highRiskHighRewardDim(plan):
    add_if_new_or_better(highRiskHighRewardDim, plan.high_risk_high_reward_score, plan)

enjoyableSkillImprovementDim = {}
def add_to_enjoyableSkillImprovementDim(plan):
    add_if_new_or_better(enjoyableSkillImprovementDim, plan.enjoyable_skill_improvement_score, plan)

def add_plan(plan):
    add_to_funAndSafeDim(plan)
    add_to_highRiskHighRewardDim(plan)
    add_to_enjoyableSkillImprovementDim(plan)

def get_random_plan():
    plans_in_map = list(enjoyableSkillImprovementDim.values())
    plans_in_map.extend(list(highRiskHighRewardDim.values()))
    plans_in_map.extend(list(highRiskHighRewardDim.values()))
    return random.choice(plans_in_map)

def get_n_best(dim, n):
    sorted_keys = sorted(dim.keys(), reverse=True)
    return sorted_keys[:n]

def get_n_best_funAndSafe(n):
    return get_n_best(funAndSafeDim, n)

def get_n_best_highRiskHighReward(n):
    return get_n_best(highRiskHighRewardDim, n)

def get_n_best_enjoyableSkillImprovement(n):
    return get_n_best(enjoyableSkillImprovementDim, n)

warmup, main, stretching = read_exercises()
next_generation = []

generator = ActivityPlanGenerator(warmup, main, stretching) 
if __name__ == '__main__':
    
    algorithmRunTime = int(input("Enter number of seconds to run MAP-Elites: "))
    startPopulationSize = int(input("Enter size of start population (Slow for querries > 100000): "))
    crossoverRate = float(input("Enter cross over rate: "))
    print('Running program. Please wait for ' + str(algorithmRunTime) + ' seconds')
    
    start_time = time.time()
    tider = []

    # Generate random activity plans

    # Place activity plans in map
    for plan in generate_activity_plans(generator, startPopulationSize):
        add_plan(plan)

    elapsed_time = time.time() - start_time
    while elapsed_time < algorithmRunTime:
        random_elite1 = get_random_plan()
        random_elite2 = get_random_plan()
        candidate = random_variation(random_elite1, random_elite2)
        add_plan(candidate)
        elapsed_time = time.time() - start_time

    print(f"Number of plans in funAndSafe dimension: {len(funAndSafeDim)}")

    for score in get_n_best_funAndSafe(3):
        plan = funAndSafeDim[score]
        #plan.print_details()
        print(f"Fun and safe score: {score}   Total score: {plan.total_score}")

    print(f"\nNumber of plans in highRiskHighReward dimension: {len(highRiskHighRewardDim)}")

    for score in get_n_best_highRiskHighReward(3):
        plan = highRiskHighRewardDim[score]
        #plan.print_details()
        print(f"High Risk High Reward score: {score}   Total score: {plan.total_score}")

    print(f"\nNumber of plans in enjoyableSkillImprovement dimension: {len(enjoyableSkillImprovementDim)}")

    for score in get_n_best_enjoyableSkillImprovement(3):
        plan = enjoyableSkillImprovementDim[score]
        #plan.print_details()
        print(f"Enjoyable Skill Improvement score: {score}   Total score: {plan.total_score}")

    # Uncomment the following to display the best plan:

    # print(f"{elapsed_time:.2f} count: {count}  The best: {best.total_score} Number of activities: {best.total_number_of_activities}")


