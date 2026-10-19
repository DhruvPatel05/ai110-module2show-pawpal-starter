from datetime import timedelta

from pawpal_system import Owner, Pet, Task, Scheduler

def test_task_completion():
    task = Task("Morning Walk", "08:00")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    pet = Pet("Buddy", "Dog")

    task = Task("Feed Breakfast", "09:00")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task
    
def test_sorting_correctness():
    owner = Owner("Dhruv")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)

    pet.add_task(Task("Breakfast", "09:00"))
    pet.add_task(Task("Morning Walk", "08:00"))
    pet.add_task(Task("Medication", "10:30"))

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    assert [task.time for task in sorted_tasks] == [
        "08:00",
        "09:00",
        "10:30"
    ]


def test_daily_recurrence():
    owner = Owner("Dhruv")
    scheduler = Scheduler(owner)

    task = Task("Morning Walk", "08:00", "daily")
    original_date = task.due_date

    task.mark_complete()
    next_task = scheduler.handle_recurring_task(task)

    assert next_task is not None
    assert next_task.due_date == original_date + timedelta(days=1)
    assert next_task.completed is False


def test_conflict_detection():
    owner = Owner("Dhruv")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)

    pet.add_task(Task("Morning Walk", "08:00"))
    pet.add_task(Task("Breakfast", "08:00"))

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1