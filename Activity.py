class Activity:
    def __init__(self, activity_type, activity_name, duration, score, injury, skill_improvement):
        self.activity_type = activity_type
        self.activity_name = activity_name
        self.duration = duration
        self.score = score
        self.injury = injury
        self.skill_improvement = skill_improvement

    def print_details(self):
        print(f"   {self.activity_type}-{self.activity_name} ({self.duration} minutter)")
