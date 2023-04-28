class ActivityPlan:

    def __init__(self, monday_workout, wednesday_workout, saturday_workout):
        self.monday_workout = monday_workout
        self.wednesday_workout = wednesday_workout
        self.saturday_workout = saturday_workout


    @property
    def main_activity_types(self):
        distinct_list = []
        for activity_type in self.monday_workout.main_activity_types:
            if activity_type not in distinct_list:
                distinct_list.append(activity_type)
        for activity_type in self.wednesday_workout.main_activity_types:
            if activity_type not in distinct_list:
                distinct_list.append(activity_type)
        for activity_type in self.saturday_workout.main_activity_types:
            if activity_type not in distinct_list:
                distinct_list.append(activity_type)
        return distinct_list

    @property
    def all_activities(self):
        activities = set()
        activities.update(self.monday_workout.all_activities)
        activities.update(self.wednesday_workout.all_activities)
        activities.update(self.saturday_workout.all_activities)
        return list(activities)

    @property
    def total_number_of_activities(self):        
        return len(self.all_activities)

    @property
    def total_number_of_activity_types(self):
        return len(self.main_activity_types)

    @property
    def total_activity_score(self):
        return self.monday_workout.activity_score + self.wednesday_workout.activity_score + self.saturday_workout.activity_score

    @property
    def total_activity_injury(self):
        return (self.monday_workout.activity_injury + self.wednesday_workout.activity_injury + self.saturday_workout.activity_injury) * -1

    @property
    def total_skill_improvement(self):
        return self.monday_workout.activity_skill_improvement + self.wednesday_workout.activity_skill_improvement + self.saturday_workout.activity_skill_improvement

    @property
    def total_duration_deviation(self):
        return (self.monday_workout.duration_deviation + self.wednesday_workout.duration_deviation + self.saturday_workout.duration_deviation) * -1

    @property
    def fun_and_safe_score(self):
        return self.total_activity_injury * -1 + self.total_activity_score

    @property
    def high_risk_high_reward_score(self):
        return self.total_activity_injury + self.total_skill_improvement

    @property
    def enjoyable_skill_improvement_score(self):
        return self.total_activity_score + self.total_skill_improvement

    @property
    def total_score(self):
        weigth_number_of_activities = 10
        weighted_number_of_activities_score = weigth_number_of_activities * self.total_number_of_activities

        weigth_number_of_activity_types = 1
        weighted_number_of_activity_types_score = weigth_number_of_activity_types * self.total_number_of_activity_types

        weigth_activity_score = 2
        weighted_activity_score = weigth_activity_score * self.total_activity_score

        weigth_activity_injury = 10
        weighted_activity_injury = weigth_activity_injury * self.total_activity_injury

        weigth_skill_improvement = 3
        weighted_skill_improvement = weigth_skill_improvement * self.total_skill_improvement
        
        weigth_duration_deviation = 5
        weighted_duration_deviation = weigth_duration_deviation * self.total_duration_deviation

        total_score = weighted_number_of_activities_score + weighted_number_of_activity_types_score + weighted_activity_score + weighted_activity_injury + weighted_skill_improvement + weighted_duration_deviation

        return total_score

        
    def print_details(self):
        print("Monday:")
        self.monday_workout.print_details()
        print("Wednesday:")
        self.wednesday_workout.print_details()
        print("Saturday:")
        self.saturday_workout.print_details()
        print("Score: " + str(self.total_score))
