from dataclasses import dataclass, field


@dataclass
class Task:
    """Represents a single pet care activity."""

    description: str
    time: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        pass


@dataclass
class Pet:
    """Represents a pet and its assigned tasks."""

    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        pass

    def get_tasks(self):
        """Return all tasks assigned to this pet."""
        pass


class Owner:
    """Represents an owner who manages multiple pets."""

    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to the owner."""
        pass

    def get_all_tasks(self):
        """Return tasks from all of the owner's pets."""
        pass


class Scheduler:
    """Organizes and manages tasks across all pets."""

    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        """Retrieve all tasks through the Owner."""
        pass

    def sort_by_time(self):
        """Sort tasks by their scheduled time."""
        pass

    def filter_tasks(self):
        """Filter tasks by pet or completion status."""
        pass

    def detect_conflicts(self):
        """Detect tasks scheduled at the same time."""
        pass

    def handle_recurring_task(self):
        """Handle creation of recurring tasks."""
        pass
    