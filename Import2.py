import csv
from Activity import *
from Workout import *
from ActivityPlan import *

def save_activity_plan_to_csv(activity_plan, filename='best.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Day', 'Type', 'Name', 'Duration', 'Score', 'Injury', 'Skill Improvement'])
        
        for day, workout in [('Monday', activity_plan.monday_workout), ('Wednesday', activity_plan.wednesday_workout), ('Saturday', activity_plan.saturday_workout)]:
            for exercise in workout.warmup_exercises:
                writer.writerow([day, 'Warm-up', exercise.activity_name, exercise.duration, exercise.score, exercise.injury, exercise.skill_improvement])
            for exercise in workout.main_exercises:
                writer.writerow([day, 'Main', exercise.activity_name, exercise.duration, exercise.score, exercise.injury, exercise.skill_improvement])
            for exercise in workout.stretching_exercises:
                writer.writerow([day, 'Stretching', exercise.activity_name, exercise.duration, exercise.score, exercise.injury, exercise.skill_improvement])

def read_activity_plan_from_csv(filename='best.csv'):
    warm_up = []
    main_exercises = []
    stretching = []

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            activity = Activity(str(row["Type"]), str(row["Name"]), int(row["Duration"]), float(row["Score"]), float(row["Injury"]), float(row["Skill Improvement"]))
            activity_type = str(row["Type"])
            if activity_type == "Warm-up":
                warm_up.append(activity)
            elif  activity_type == "Stretching":
                stretching.append(activity)
            else:
                main_exercises.append(activity)

    monday_warmup_exercises = [exercise for exercise in warm_up if row["Day"] == "Monday"]
    wednesday_warmup_exercises = [exercise for exercise in warm_up if row["Day"] == "Wednesday"]
    saturday_warmup_exercises = [exercise for exercise in warm_up if row["Day"] == "Saturday"]
    monday_main_exercises = [exercise for exercise in main_exercises if row["Day"] == "Monday"]
    wednesday_main_exercises = [exercise for exercise in main_exercises if row["Day"] == "Wednesday"]
    saturday_main_exercises = [exercise for exercise in main_exercises if row["Day"] == "Saturday"]
    monday_stretching_exercises = [exercise for exercise in stretching if row["Day"] == "Monday"]
    wednesday_stretching_exercises = [exercise for exercise in stretching if row["Day"] == "Wednesday"]
    saturday_stretching_exercises = [exercise for exercise in stretching if row["Day"] == "Saturday"]

    monday_workout = Workout(monday_warmup_exercises, monday_main_exercises, monday_stretching_exercises)
    wednesday_workout = Workout(wednesday_warmup_exercises, wednesday_main_exercises, wednesday_stretching_exercises)
    saturday_workout = Workout(saturday_warmup_exercises, saturday_main_exercises, saturday_stretching_exercises)
    return ActivityPlan(monday_workout, wednesday_workout, saturday_workout)

def read_exercises():
    warm_up = []
    main_exercises = []
    stretching = []

    csv_file = "./data/drills_space.csv"

    # Open the CSV file and read the data
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            activity = Activity(str(row["Activity Type"]), str(row["Type"]), int(row["Duration"]), float(row["Score"]), float(row["Injuries"]), float(row["SkillImprovement"]))
            activity_type = str(row["Activity Type"])
            if activity_type == "Warm-up Exercises":
                warm_up.append(activity)
            elif  activity_type == "Stretching":
                stretching.append(activity)
            else:
                main_exercises.append(activity)

    return warm_up, main_exercises, stretching

if __name__ == '__main__':
    warmup, main, stretching = read_exercises()

    for a in main:
        a.print_activity_details()
