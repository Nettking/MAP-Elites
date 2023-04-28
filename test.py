from Import2 import *
from ActivityPlanGenerator import *


def generate_activity_plans(generator, number_of_plans):
    activity_plans = []
    for i in range(0, number_of_plans):
        activity_plans.append(generator.generate_random_activity_plan())
    return activity_plans

def get_best_plans(plans, number_of_plans_to_get):
    sorted_plans = sorted(plans, key=lambda plan: plan.total_score, reverse=True)
    return sorted_plans[:int(number_of_plans_to_get)]

warmup, main, stretching = read_exercises()
next_generation = []

generator = ActivityPlanGenerator(warmup, main, stretching) 
if __name__ == '__main__':
    count = 0
    while count < 100:
        count += 1    
        
        # Generate 100 random activity plans
        plans = generate_activity_plans(generator, 2)
        
        if count > 1:
            for plan in next_generation:
                plans.append(plan)
        else:
            plans.append(read_activity_plan_from_csv())
        
        # Get the 100 best plans
        best = get_best_plans(plans, 2)

        # Perform crossover on the 100 best plans to create the next generation of plans
        plan1 = best[0]
        plan2 = best[1]
        crossover = ActivityPlanGenerator.crossover(plan1, plan2)
        best_of_three = []
        best_of_three.append(plan1)
        best_of_three.append(plan2)
        best_of_three.append(crossover)
        best_candidate = get_best_plans(best_of_three, 1)
        next_generation.append(best_candidate[0])
        # Get the 2 best plans from the next generation
        best_next_generation = get_best_plans(next_generation, 1)
        print('Current best:' + str(best_next_generation[0].total_score))
    best_next_generation[0].print_details()
    save_activity_plan_to_csv(best_next_generation[0])
    