from .models import *

class ClassificatorTask:
    project_slug = None

    def __init__(self, project_slug):
        self.project_slug = project_slug
    
    def get_distance(self, task, test_development_time, test_validation_time, test_blocking_time):
        development_time = task.development_time
        validation_time = task.validation_time
        blocking_time = task.blocking_time
        
        square_development_time = (test_development_time - development_time) ** 2
        square_validation_time = (test_validation_time - validation_time) ** 2
        square_blocking_time = (test_blocking_time - blocking_time) ** 2
        sum_squares = square_development_time + square_validation_time + square_blocking_time
        distance = sum_squares ** (1/2)
        return distance

    def get_complexity_suggestion(self, test_development_time=0, test_validation_time=0, test_blocking_time=0):
        projects = Project.objects.filter(slug=self.project_slug)
        complexity_suggestion = {}
        if projects:
            project = projects[0]
            tasks = project.tasks.all()
            smaller_test_distance = 100000000
            most_similarity_task = None
            for task in tasks:
                test_distance = self.get_distance(task, test_development_time, test_validation_time, test_blocking_time)
                if test_distance <= smaller_test_distance:
                    smaller_test_distance = test_distance
                    most_similarity_task = task
            if most_similarity_task:
                complexity_suggestion = most_similarity_task.complexity
        return complexity_suggestion