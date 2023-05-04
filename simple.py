import time
from operator import attrgetter
from Import import *
from ActivityPlanGenerator import *


def generate_activity_plans(generator, number_of_plans):
    activity_plans = []
    for i in range(0, number_of_plans):
        activity_plans.append(generator.generate_random_activity_plan())
    return activity_plans

def get_best_plans(plans, number_of_plans_to_get, attribute):
    sorted_plans = sorted(plans, key=attrgetter(attribute), reverse=True)
    return sorted_plans[:int(number_of_plans_to_get)]
print('Running program. Please wait for 1 minute')
warmup, main, stretching = read_exercises()
next_generation = []

generator = ActivityPlanGenerator(warmup, main, stretching) 
if __name__ == '__main__':
    start_time = time.time()
    optimized_plans = generate_activity_plans(generator, 10)
    while (time.time() - start_time) < 59:
        next_generation = []
        for i in range(len(optimized_plans)-1):
            plan1 = optimized_plans[i]
            plan2 = optimized_plans[i+1]
            crossover = ActivityPlanGenerator.crossover(plan1, plan2)
            mutation = generator.mutate(crossover)

            candidates = []
            candidates.append(plan1)
            candidates.append(plan2)
            candidates.append(crossover)
            if random.random() < 0.1: candidates.append(mutation)
            best_candidate = get_best_plans(candidates, 1, "total_score")[0]
            next_generation.append(best_candidate)
        next_generation.append(generator.generate_random_activity_plan())
        optimized_plans = next_generation

    print("3 best fun_and_safe")
    best_fun_and_safe = get_best_plans(optimized_plans, 3, "fun_and_safe_score")
    for plan in best_fun_and_safe:
        print(f"Fun and safe score: {plan.fun_and_safe_score}   Total score: {plan.total_score}")

    print("3 best high_risk_high_reward")
    best_high_risk_high_reward = get_best_plans(optimized_plans, 3, "high_risk_high_reward_score")
    for plan in best_high_risk_high_reward:
        print(f"High Risk High Reward score: {plan.high_risk_high_reward_score}   Total score: {plan.total_score}")

    print("3 best enjoyable_skill_improvement")
    best_enjoyable_skill_improvement = get_best_plans(optimized_plans, 3, "enjoyable_skill_improvement_score")
    for plan in best_enjoyable_skill_improvement:
        print(f"Enjoyable Skill Improvement score: {plan.enjoyable_skill_improvement_score}   Total score: {plan.total_score}")
