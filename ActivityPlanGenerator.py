import random
import copy
from Activity import *
from Workout import *
from ActivityPlan import *

class ActivityPlanGenerator:

    def __init__(self, all_warmup_exercises, all_main_exercises, all_stretching_exercises):
        self.all_warmup_exercises = all_warmup_exercises
        self.all_main_exercises = all_main_exercises
        self.all_stretching_exercises = all_stretching_exercises

    def is_not_added(self, exercises, new_exercise):
        for exercise in exercises:
            if exercise.activity_type == new_exercise.activity_type and exercise.activity_name == new_exercise.activity_name:
                return False
        return True

    def get_exercise_not_already_added(self, exercises, all_exercises):
        done = False
        while done==False:
            new_exercise = random.choice([x for x in all_exercises if x not in exercises])
            if self.is_not_added(exercises, new_exercise):
                done = True
        return(new_exercise)

    def calculate_duration(self, exercises):
        duration = 0
        for exercise in exercises:
            duration += exercise.duration
        return duration

    def generate_random_warmup_exercises(self):
        exercises = []
        while self.calculate_duration(exercises) < 15:
            exercises.append(self.get_exercise_not_already_added(exercises, self.all_warmup_exercises))
        return exercises

    def generate_random_main_exercises(self):
        exercises = []
        while self.calculate_duration(exercises) < 60:
            exercises.append(self.get_exercise_not_already_added(exercises, self.all_main_exercises))
        return exercises

    def generate_random_stretching_exercises(self):
        exercises = []
        while self.calculate_duration(exercises) < 15:
            exercises.append(self.get_exercise_not_already_added(exercises, self.all_stretching_exercises)) 
        return exercises

    def generate_random_workout(self):
        warmup_exercises = self.generate_random_warmup_exercises()
        main_exercises = self.generate_random_main_exercises()
        stretching_exercises = self.generate_random_stretching_exercises()
        return Workout(warmup_exercises, main_exercises, stretching_exercises)

    def generate_random_activity_plan(self):
        monday_workout = self.generate_random_workout()
        wednesday_workout = self.generate_random_workout()
        saturday_workout = self.generate_random_workout()
        return ActivityPlan(monday_workout, wednesday_workout, saturday_workout)

    def mutate_workout(self, workout):
        parts = ['warmup', 'main', 'stretching']
        random_part = random.choice(parts)

        mutated_workout = copy.deepcopy(workout)
        if (random_part == 'warmup'):
            mutated_workout.warmup_exercises = self.generate_random_warmup_exercises()
        elif (random_part == 'main'):
            mutated_workout.main_exercises = self.generate_random_main_exercises()
        elif (random_part == 'stretching'):
            mutated_workout.stretching_exercises = self.generate_random_stretching_exercises()
        return mutated_workout

    def mutate(self, plan):
        random_day = random.randint(1, 3)
        workout_dict = {
            1: ('Monday', 'monday_workout'),
            2: ('Wednesday', 'wednesday_workout'),
            3: ('Saturday', 'saturday_workout')
        }
        day, attr_name = workout_dict[random_day]
        new_workout = self.mutate_workout(getattr(plan, attr_name))
        setattr(plan, attr_name, new_workout)
        return plan

    @staticmethod
    def activity_in_list(activities, activity):
        for act in activities:
            if (activity.activity_type == act.activity_type and activity.activity_name == act.activity_name): 
                return True
        return False

    @staticmethod
    def activities_not_in_list(dominent_activities, recessive_activities):
        result = []
        for activity in recessive_activities:
            if not ActivityPlanGenerator.activity_in_list(dominent_activities, activity):
                result.append(activity)
        return result

    @staticmethod
    def crossover_activity_list(dominent_activities, recessive_activities):
        result = copy.copy(recessive_activities)
        return result

    @staticmethod
    def crossover_day(dominent_day, recessive_day):
        result = copy.deepcopy(dominent_day)
        parts = ['warmup', 'main', 'stretching']
        random_part = random.choice(parts)
        setattr(result, f'{random_part}_exercises', ActivityPlanGenerator.crossover_activity_list(getattr(dominent_day, f'{random_part}_exercises'), getattr(recessive_day, f'{random_part}_exercises')))
        return result

    @staticmethod
    def crossover(activity_plan1, activity_plan2):

        if (activity_plan1.total_score > activity_plan2.total_score):
            dominent = activity_plan1
            rescesive = activity_plan2
        else:
            dominent = activity_plan2
            rescesive = activity_plan1

        result = copy.deepcopy(dominent)

        random_day = random.randint(1, 3)

        workout_dict = {
            1: ('Monday', 'monday_workout'),
            2: ('Wednesday', 'wednesday_workout'),
            3: ('Saturday', 'saturday_workout')
        }

        day, attr_name = workout_dict[random_day]
        workout = ActivityPlanGenerator.crossover_day(getattr(dominent, attr_name), getattr(rescesive, attr_name))
        setattr(result, attr_name, workout)
        return result
    