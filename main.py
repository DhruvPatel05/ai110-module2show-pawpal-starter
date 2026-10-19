from pawpal_system import Owner, Pet, Task, Scheduler


# Create an owner
owner = Owner("Dhruv")

# Create two pets
dog = Pet("Buddy", "Dog")
cat = Pet("Luna", "Cat")

# Add pets to the owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create at least three tasks
dog.add_task(Task("Morning Walk", "08:00", "daily"))
dog.add_task(Task("Feed Breakfast", "09:00", "daily"))
cat.add_task(Task("Give Medication", "10:30", "daily"))

# Create the scheduler
scheduler = Scheduler(owner)

# Display today's schedule
print("=== Today's Schedule ===")

for task in scheduler.get_all_tasks():
    status = "Completed" if task.completed else "Pending"

    print(
        f"{task.time} | "
        f"{task.description} | "
        f"{task.frequency} | "
        f"{status}"
    )