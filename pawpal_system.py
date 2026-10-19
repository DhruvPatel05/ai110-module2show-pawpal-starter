from dataclasses import dataclass, field
from datetime import date, timedelta

@dataclass
class Task:
    """Represents a single pet care activity."""

    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True
        
    


@dataclass
class Pet:
    """Represents a pet and its assigned tasks."""

    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks assigned to this pet."""
        return self.tasks


class Owner:
    """Represents an owner who manages multiple pets."""

    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return tasks from all of the owner's pets."""
        all_tasks = []

        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())

        return all_tasks


class Scheduler:
    """Organizes and manages tasks across all pets."""

    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        """Retrieve all tasks through the Owner."""
        return self.owner.get_all_tasks()

    def sort_by_time(self):
        """Return all tasks sorted by scheduled time."""
        return sorted(
            self.get_all_tasks(),
            key=lambda task: task.time
        )

    def filter_tasks(self, completed=None):
        """Filter tasks by completion status."""
        tasks = self.get_all_tasks()

        if completed is None:
            return tasks

        return [
            task
            for task in tasks
            if task.completed == completed
        ]

    def detect_conflicts(self):
        """Return pairs of tasks scheduled at the same time."""
        tasks = self.get_all_tasks()
        conflicts = []

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                if tasks[i].time == tasks[j].time:
                    conflicts.append((tasks[i], tasks[j]))

        return conflicts

    def handle_recurring_task(self, task):
        """Create the next occurrence of a recurring task."""

        if task.frequency == "daily":
            next_date = task.due_date + timedelta(days=1)

        elif task.frequency == "weekly":
            next_date = task.due_date + timedelta(days=7)

        else:
            return None

        return Task(
            description=task.description,
            time=task.time,
            frequency=task.frequency,
            completed=False,
            due_date=next_date
        )