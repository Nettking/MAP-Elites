class Workout:

    def __init__(self, warmup_exercises, main_exercises, stretching_exercises):
        self.warmup_exercises = warmup_exercises
        self.main_exercises = main_exercises
        self.stretching_exercises = stretching_exercises

    @property        
    def all_activities(self):
        activities = []
        activities.extend(self.warmup_exercises)
        activities.extend(self.main_exercises)
        activities.extend(self.stretching_exercises)
        return activities

    @property        
    def warmup_duration(self):
        return self.calculate_duration(self.warmup_exercises)
        
    @property        
    def main_duration(self):
        return self.calculate_duration(self.main_exercises)

    @property
    def main_activity_types(self):
        distinct_list = []
        for exercise in self.main_exercises:
            if exercise.activity_type not in distinct_list:
                distinct_list.append(exercise.activity_type)
        return distinct_list

    @property        
    def stretching_duration(self):
        return self.calculate_duration(self.stretching_exercises)

    def print_details(self):
        print(f" Warmup ({self.warmup_duration} minutter): ")
        for exercise in self.warmup_exercises:
            exercise.print_details()
        print(f" Main ({self.main_duration} minutter):")
        for exercise in self.main_exercises:
            exercise.print_details()
        print(f" Stretching ({self.stretching_duration} minutter):")
        for exercise in self.stretching_exercises:
            exercise.print_details()

    def calculate_duration(self, exercises):
        duration = 0
        for exercise in exercises:
            duration += exercise.duration
        return duration

    def calculate_score(self, exercises):
        score = 0
        for exercise in exercises:
            score += exercise.score
        return score

    def calculate_injury(self, exercises):
        injury = 0
        for exercise in exercises:
            injury += exercise.injury
        return injury

    def calculate_skill_improvement(self, exercises):
        skill_improvement = 0
        for exercise in exercises:
            skill_improvement += exercise.skill_improvement
        return skill_improvement

    def calculate_duration_deviation(self, exercises, expected_duration):
        deviation = abs(expected_duration - self.calculate_duration(exercises))
        return deviation

    @property
    def activity_score(self):
        return self.calculate_score(self.warmup_exercises) + self.calculate_score(self.main_exercises) + self.calculate_score(self.stretching_exercises)

    @property
    def activity_injury(self):
        return self.calculate_injury(self.warmup_exercises) + self.calculate_injury(self.main_exercises) + self.calculate_injury(self.stretching_exercises)

    @property
    def activity_skill_improvement(self):
        return self.calculate_skill_improvement(self.warmup_exercises) + self.calculate_skill_improvement(self.main_exercises) + self.calculate_skill_improvement(self.stretching_exercises)

    @property
    def duration_deviation(self):
        return self.calculate_duration_deviation(self.warmup_exercises, 15) + self.calculate_duration_deviation(self.main_exercises, 60) + self.calculate_duration_deviation(self.stretching_exercises, 15)
