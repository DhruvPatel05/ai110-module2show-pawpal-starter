# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pets.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks such as walks, feeding, medications, enrichment, grooming, and appointments
- Manage multiple pets
- Organize tasks by scheduled time
- Track task completion and recurring activities
- Produce a daily plan for pet care

The system is designed using object-oriented programming with separate classes for owners, pets, tasks, and scheduling.

## What You Will Build

The final PawPal+ app will:

- Let a user manage owner and pet information
- Support multiple pets
- Let a user create pet care tasks
- Track task time, frequency, and completion status
- Generate an organized daily schedule
- Support sorting and filtering
- Detect scheduling conflicts
- Handle recurring tasks
- Display the schedule through a Streamlit interface
- Include automated tests for important behaviors

## Getting Started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the command-line demonstration with:

```bash
python main.py
```

Run the tests with:

```bash
python -m pytest
```

## Implementation Summary

PawPal+ currently uses four main classes:

- **Task** represents an individual pet care activity. It stores the task description, scheduled time, frequency, and completion status.
- **Pet** stores information about an individual pet and manages the tasks assigned to that pet.
- **Owner** manages multiple pets and provides access to tasks across all of the owner's pets.
- **Scheduler** works through the Owner to retrieve and organize tasks across multiple pets.

The main backend logic is located in `pawpal_system.py`.

The `main.py` file provides a command-line demonstration that creates an owner, multiple pets, and several pet care tasks.

The system currently supports adding pets, adding tasks, retrieving tasks across multiple pets, and marking tasks as completed.

## 🖥️ Sample Output

Running:

```bash
python main.py
```

currently produces:

```text
=== Today's Schedule ===
08:00 | Morning Walk | daily | Pending
09:00 | Feed Breakfast | daily | Pending
10:30 | Give Medication | daily | Pending
```

This demonstrates that the Scheduler can retrieve tasks belonging to multiple pets through the Owner.

## 🧪 Testing PawPal+

Run the current test suite with:

```bash
python -m pytest
```

Current test output:

```text
============================= test session starts ==============================
collected 2 items

tests/test_pawpal.py ..                                             [100%]

============================== 2 passed ===============================
```

The current tests verify:

- **Task completion:** `Task.mark_complete()` correctly changes a task from incomplete to completed.
- **Task addition:** `Pet.add_task()` correctly adds a task to a pet's task list.

Additional scheduling tests will be added as the scheduling algorithms are implemented.

## 📐 Smarter Scheduling

PawPal+ includes several scheduling algorithms that organize and manage pet care tasks.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts tasks chronologically using their `HH:MM` scheduled time |
| Filtering | `Scheduler.filter_tasks()` | Filters tasks based on completion status |
| Conflict handling | `Scheduler.detect_conflicts()` | Detects tasks that are scheduled at the exact same time and returns conflict pairs |
| Recurring tasks | `Scheduler.handle_recurring_task()` | Creates the next occurrence one day later for daily tasks and seven days later for weekly tasks |

## 📸 Demo Walkthrough

Current command-line workflow:

1. Create an `Owner`.
2. Create multiple `Pet` objects and add them to the owner.
3. Create pet care `Task` objects with different scheduled times.
4. Assign the tasks to the appropriate pets.
5. Create a `Scheduler` connected to the owner.
6. Retrieve tasks across the owner's pets.
7. Display the tasks as a daily schedule.

The next stage of the project will connect this backend logic to the Streamlit user interface.

**Screenshot or video (optional):** A Streamlit demonstration can be added after the UI integration is complete.
