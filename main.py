from pawpal_system import Owner, Pet, Task, Scheduler


# Create owner
owner = Owner("Dhruv")

# Create pets
dog = Pet("Buddy", "Dog")
cat = Pet("Luna", "Cat")

owner.add_pet(dog)
owner.add_pet(cat)


# Add tasks OUT OF ORDER to test sorting
dog.add_task(Task("Feed Breakfast", "09:00", "daily"))
dog.add_task(Task("Morning Walk", "08:00", "daily"))
cat.add_task(Task("Give Medication", "10:30", "daily"))

# Same time as Morning Walk to test conflict detection
cat.add_task(Task("Feed Luna", "08:00", "daily"))


scheduler = Scheduler(owner)


# -------------------------
# SORTING
# -------------------------

print("=== Sorted Schedule ===")

for task in scheduler.sort_by_time():
    status = "Completed" if task.completed else "Pending"

    print(
        f"{task.time} | "
        f"{task.description} | "
        f"{task.frequency} | "
        f"{status}"
    )


# -------------------------
# FILTERING
# -------------------------

print("\n=== Pending Tasks ===")

for task in scheduler.filter_tasks(completed=False):
    print(f"{task.time} | {task.description}")


# -------------------------
# CONFLICT DETECTION
# -------------------------

print("\n=== Conflicts ===")

conflicts = scheduler.detect_conflicts()

if conflicts:
    for task1, task2 in conflicts:
        print(
            f"WARNING: {task1.description} and "
            f"{task2.description} are both scheduled "
            f"at {task1.time}"
        )
else:
    print("No scheduling conflicts.")

# -------------------------
# RECURRING TASK
# -------------------------

print("\n=== Recurring Task ===")

daily_task = Task(
    "Evening Walk",
    "18:00",
    "daily"
)

print(f"Current occurrence: {daily_task.due_date}")

daily_task.mark_complete()

next_task = scheduler.handle_recurring_task(daily_task)

if next_task:
    print(f"Next occurrence: {next_task.due_date}")