from subject import Subject


class Teach:
    instance = []

    def __init__(self, day, period, subject, teacher_name):
        self.day = day
        self.period = period
        self.teacher_name = teacher_name

        self.subject = subject
