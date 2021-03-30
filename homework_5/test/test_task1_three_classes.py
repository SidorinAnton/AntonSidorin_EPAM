import datetime

import pytest

import homework_5.src.task1_three_classes as task1

# Test from task


def test_from_task_of_teacher_class():
    teacher = task1.Teacher("Daniil", "Shadrin")
    assert teacher.last_name == "Daniil"


def test_from_task_of_student_class():
    student = task1.Student("Roman", "Petrov")
    assert student.first_name == "Petrov"


def test_from_task_of_expired_homework_text():
    expired_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "Learn functions", 0
    )

    assert expired_homework.text == "Learn functions"


def test_from_task_of_expired_homework_deadline():
    expired_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "Learn functions", 0
    )

    assert expired_homework.deadline == datetime.timedelta(0)


def test_from_task_of_expired_homework_created(monkeypatch):
    class MockTime:
        def __init__(self, *args):
            self.created = datetime.datetime.strptime("2019-05-26", "%Y-%m-%d")

    monkeypatch.setattr(task1, "Homework", MockTime)
    expired_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "Learn functions", 0
    )

    assert expired_homework.created == datetime.datetime.strptime(
        "2019-05-26", "%Y-%m-%d"
    )


def test_from_task_from_method_and_use_it_homework():
    create_homework_too = task1.Teacher("Daniil", "Shadrin").create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert oop_homework.deadline == datetime.timedelta(5)


def test_from_task_do_homework_in_process():
    oop_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "create 2 simple classes", 5
    )
    student = task1.Student("Roman", "Petrov")

    assert isinstance(student.do_homework(oop_homework), task1.Homework)


def test_from_task_do_homework_late_type():
    expired_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "Learn functions", 0
    )
    student = task1.Student("Roman", "Petrov")

    assert student.do_homework(expired_homework) is None


def test_from_task_do_homework_late_stdout(capsys):
    expired_homework = task1.Teacher("Daniil", "Shadrin").create_homework(
        "Learn functions", 0
    )
    student = task1.Student("Roman", "Petrov")
    student.do_homework(expired_homework)
    captured = capsys.readouterr()

    assert captured.out == "You are late\n"


# My tests
@pytest.mark.parametrize(["deadline", "is_active"], [(5, True), (2, True)])
def test_my_test_teacher_creates_homework(deadline, is_active):
    teacher = task1.Teacher("Some", "name")
    student = task1.Student("Another", "name")

    homework = teacher.create_homework("Some task", deadline)
    progress_of_hw = student.do_homework(homework)

    assert progress_of_hw.is_active() == is_active
