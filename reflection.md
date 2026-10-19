# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial design for PawPal+ uses four main classes: Owner, Pet, Task, and Scheduler. The goal is to keep each class responsible for a specific part of the pet care management system.

The three core actions a user should be able to perform are:

1. Add and manage multiple pets.
2. Schedule tasks such as feeding, walking, medication, and appointments for a pet.
3. View and manage a daily schedule, including marking tasks as completed.

The classes and their responsibilities are:

- **Owner:** Stores the owner's information and manages multiple pets. It also provides access to tasks from all of the owner's pets.
- **Pet:** Stores information about an individual pet and manages the tasks assigned to that pet.
- **Task:** Represents a pet care activity. It stores information such as the task description, time, frequency, completion status, and due date.
- **Scheduler:** Retrieves tasks through the Owner and organizes them across multiple pets. It handles sorting, filtering, recurring tasks, and scheduling conflict detection.

The main relationships in my design are that one Owner can have multiple Pets, each Pet can have multiple Tasks, and the Scheduler works with the Owner to access and organize tasks across all pets.

**b. Design changes**

Yes, my design changed during implementation. One important change was adding a `due_date` attribute to the `Task` class.

My original design only stored the task's time and frequency. When I implemented recurring tasks, I realized the system needed an actual date so it could calculate the next occurrence of a daily or weekly task.

I also expanded the `Scheduler` class with methods for sorting, filtering, conflict detection, and recurring-task handling. These changes made the final class design better match the functionality required by PawPal+.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler currently considers scheduled time, completion status, task frequency, and scheduling conflicts.

Tasks are sorted chronologically using their scheduled time in `HH:MM` format. Tasks can also be filtered according to completion status. The task frequency determines whether a recurring task should occur daily or weekly.

For recurring tasks, a daily task receives a next occurrence one day later, while a weekly task receives a next occurrence seven days later.

I focused primarily on time and completion status because these constraints are important for creating a simple and understandable daily pet care schedule.

**b. Tradeoffs**

One tradeoff in my scheduler is that conflict detection only checks whether two tasks have exactly the same scheduled time.

For example, two tasks scheduled at `08:00` are considered a conflict. However, the current system does not calculate whether tasks overlap based on their duration.

This tradeoff is reasonable for the current version because exact-time conflict detection is simple, predictable, and easy for the user to understand. A future version could include task duration and detect overlapping time ranges.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI throughout the project for design brainstorming, creating the initial UML structure, scaffolding the Python classes, debugging code, developing scheduling algorithms, and creating automated tests.

I used AI to help determine how the `Scheduler` should retrieve tasks from multiple pets through the `Owner`. I also used it to understand how to sort tasks stored in `HH:MM` format and how to implement a lightweight conflict-detection algorithm.

Specific prompts about one problem at a time were the most useful because they made the suggestions easier to understand, test, and integrate into the project.

**b. Judgment and verification**

I did not accept every AI suggestion without checking it.

One example occurred while implementing the scheduling methods. A method was placed at the wrong indentation level, which caused Python to report that the `Scheduler` object did not have the `handle_recurring_task` method.

Instead of assuming the generated code was correct, I read the traceback, inspected the class structure, corrected the indentation and method placement, and reran the program.

I verified AI-assisted code by running the CLI demonstration, testing the Streamlit interface, and creating automated tests with pytest. This helped confirm that the implementation actually behaved as expected.

---

## 4. Testing and Verification

**a. What you tested**

I created automated tests for five important behaviors:

- Marking a task as completed
- Adding a task to a pet
- Sorting tasks chronologically
- Creating the next occurrence of a daily recurring task
- Detecting tasks scheduled at the same time

These tests are important because they verify both the basic behavior of the classes and the main scheduling algorithms.

I also manually tested the application through `main.py` and the Streamlit interface. In the Streamlit app, I verified that tasks were displayed chronologically and that a warning appeared when two tasks were scheduled at the same time.

**b. Confidence**

My confidence level in the current scheduler is **5/5**.

All five automated tests pass, and I also verified the scheduling functionality using the command-line demonstration and Streamlit interface.

If I had more time, I would test additional edge cases such as:

- An owner with no pets
- A pet with no tasks
- Weekly recurrence
- Duplicate pet names
- Invalid or unusual task times
- Multiple conflicts at the same time
- Overlapping tasks with different start times and durations

---

## 5. Reflection

**a. What went well**

I am most satisfied with connecting the object-oriented backend to the Streamlit interface.

The application uses the same `Owner`, `Pet`, `Task`, and `Scheduler` objects in both the backend and the user interface. The Scheduler can sort tasks, filter tasks, detect conflicts, and create recurring task occurrences.

I am also satisfied that I created automated tests instead of relying only on manual testing.

**b. What you would improve**

If I had another iteration, I would add task duration and priority.

Adding duration would allow the scheduler to identify overlapping time ranges instead of detecting only tasks with identical start times. Adding priority could allow important tasks such as medications to receive higher scheduling priority.

I would also add persistent storage so that owners, pets, and tasks remain saved after the Streamlit application is closed.

**c. Key takeaway**

One important thing I learned is that designing the relationships between classes before implementing the user interface makes the system easier to organize and maintain.

I also learned that AI-generated code still requires human judgment and verification. Running the program, reading error messages, checking the design, and writing automated tests were necessary to make sure the suggested code actually worked correctly.