# PawPal+ (Module 2 Project)

**PawPal+** is a Streamlit application that helps pet owners organize and manage daily care tasks for multiple pets.

## Scenario

A busy pet owner needs help staying consistent with pet care. PawPal+ helps the owner:

- Track pet care tasks such as walks, feeding, medications, enrichment, grooming, and appointments
- Manage multiple pets
- Organize tasks by scheduled time
- Track task completion and recurring activities
- Detect scheduling conflicts
- Produce an organized daily pet care schedule

The system uses object-oriented programming with separate classes for owners, pets, tasks, and scheduling.

## Features

PawPal+ allows users to:

- Add and manage an owner
- Add multiple pets
- Create care tasks for individual pets
- Assign a scheduled time to each task
- Choose task frequency: once, daily, or weekly
- Track task completion status
- View tasks from multiple pets
- Sort tasks chronologically
- Filter tasks by completion status
- Detect tasks scheduled at the same time
- Generate the next occurrence of daily and weekly tasks
- Generate a daily schedule through a Streamlit interface
- Display scheduling conflict warnings

## Getting Started

### Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the command-line demonstration:

```bash
python main.py
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Run the automated tests:

```bash
python -m pytest
```

## Implementation Summary

PawPal+ uses four main classes:

- **Task** represents an individual pet care activity. It stores the task description, scheduled time, frequency, completion status, and due date.
- **Pet** stores information about an individual pet and manages the tasks assigned to that pet.
- **Owner** manages multiple pets and provides access to tasks across all of the owner's pets.
- **Scheduler** retrieves tasks through the Owner and provides sorting, filtering, conflict detection, and recurring-task functionality.

The backend logic is implemented in `pawpal_system.py`.

The `main.py` file provides a command-line demonstration of the scheduling algorithms.

The `app.py` file provides the Streamlit user interface and stores the Owner object in `st.session_state` so pet and task information remains available while the application reruns.

## 🖥️ Sample Output

Running:

```bash
python main.py
```

produces output similar to:

```text
=== Sorted Schedule ===
08:00 | Morning Walk | daily | Pending
08:00 | Feed Luna | daily | Pending
09:00 | Feed Breakfast | daily | Pending
10:30 | Give Medication | daily | Pending

=== Pending Tasks ===
09:00 | Feed Breakfast
08:00 | Morning Walk
10:30 | Give Medication
08:00 | Feed Luna

=== Conflicts ===
WARNING: Morning Walk and Feed Luna are both scheduled at 08:00

=== Recurring Task ===
Current occurrence: 2026-10-18
Next occurrence: 2026-10-19
```

This demonstrates chronological sorting, filtering, conflict detection, and recurring-task behavior.

## 🧪 Testing PawPal+

Run the complete test suite with:

```bash
python -m pytest
```

The automated tests verify:

- Task completion
- Adding tasks to pets
- Chronological task sorting
- Daily recurrence logic
- Scheduling conflict detection

Latest test result:

```text
============================= test session starts ==============================
collected 5 items

tests/test_pawpal.py .....                                            [100%]

============================== 5 passed ===============================
```

**Confidence Level:** ⭐⭐⭐⭐⭐ (5/5)

All currently implemented core scheduling behaviors pass the automated tests.

## 📐 Smarter Scheduling

PawPal+ includes several scheduling algorithms that organize and manage pet care tasks.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts tasks chronologically using their `HH:MM` scheduled time |
| Filtering | `Scheduler.filter_tasks()` | Filters tasks based on completion status |
| Conflict handling | `Scheduler.detect_conflicts()` | Detects tasks scheduled at the exact same time and returns conflict pairs |
| Recurring tasks | `Scheduler.handle_recurring_task()` | Creates the next occurrence one day later for daily tasks and seven days later for weekly tasks |

### Scheduling Tradeoff

Conflict detection currently checks whether two tasks have the exact same scheduled time. It does not calculate overlapping task durations. This keeps the algorithm simple and understandable while still identifying obvious scheduling conflicts.

## 📸 Demo Walkthrough

1. Open the PawPal+ Streamlit application.
2. Enter the owner's name and click **Save Owner**.
3. Add one or more pets by entering a pet name and selecting its species.
4. Select a pet and create a care task by entering its description, scheduled time, and frequency.
5. View all added tasks in the **Current Tasks** table.
6. Add additional tasks for the same or different pets.
7. Click **Generate Schedule**.
8. PawPal+ displays the tasks in chronological order.
9. If two tasks are scheduled at the same time, the application displays a scheduling conflict warning.
10. Daily and weekly recurring tasks can generate their next occurrence using the Scheduler.

### Example Workflow

For example, an owner can add a dog named Buddy and create the following tasks:

```text
09:00 — Breakfast
08:00 — Morning Walk
08:00 — Medication
```

Even though Breakfast was added first, PawPal+ sorts the generated schedule chronologically:

```text
08:00 — Morning Walk
08:00 — Medication
09:00 — Breakfast
```

Because Morning Walk and Medication are both scheduled at `08:00`, PawPal+ also displays a conflict warning.

## Project Structure

```text
pawpal_system.py       Core OOP classes and scheduling algorithms
main.py                Command-line demonstration
app.py                 Streamlit user interface
tests/test_pawpal.py   Automated tests
diagrams/uml.mmd       UML class diagram
reflection.md          Project reflection
ai_interactions.md     AI collaboration documentation
requirements.txt       Python dependencies
```
