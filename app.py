import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler


if st.button("Reset App"):
    st.session_state.clear()
    st.rerun()
st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")
st.write("Smart pet care planning for your furry friends.")


# -------------------------
# SESSION STATE
# -------------------------

if "owner" not in st.session_state:
    st.session_state.owner = None


# -------------------------
# OWNER
# -------------------------

st.header("👤 Owner Information")

with st.form("owner_form"):
    owner_name = st.text_input("Owner name")
    save_owner = st.form_submit_button("Save Owner")

    if save_owner:
        if owner_name.strip():
            if st.session_state.owner is None:
                st.session_state.owner = Owner(owner_name.strip())
            else:
                st.session_state.owner.name = owner_name.strip()

            st.success(f"Owner saved: {owner_name}")
        else:
            st.warning("Please enter an owner name.")


# -------------------------
# ADD PET
# -------------------------

st.divider()
st.header("🐶 Add a Pet")

with st.form("pet_form"):
    pet_name = st.text_input("Pet name")

    species = st.selectbox(
        "Species",
        ["Dog", "Cat", "Bird", "Other"]
    )

    add_pet = st.form_submit_button("Add Pet")

    if add_pet:
        if st.session_state.owner is None:
            st.warning("Please save the owner first.")

        elif not pet_name.strip():
            st.warning("Please enter a pet name.")

        else:
            new_pet = Pet(
                name=pet_name.strip(),
                species=species
            )

            st.session_state.owner.add_pet(new_pet)

            st.success(f"{new_pet.name} added successfully!")


# -------------------------
# DISPLAY PETS
# -------------------------

if st.session_state.owner and st.session_state.owner.pets:
    st.subheader("Your Pets")

    for pet in st.session_state.owner.pets:
        st.write(f"🐾 **{pet.name}** — {pet.species}")


# -------------------------
# ADD TASK
# -------------------------

st.divider()
st.header("📝 Add a Care Task")

if st.session_state.owner and st.session_state.owner.pets:

    pet_names = [
        pet.name
        for pet in st.session_state.owner.pets
    ]

    with st.form("task_form"):

        selected_pet_name = st.selectbox(
            "Select pet",
            pet_names
        )

        task_description = st.text_input(
            "Task description"
        )

        task_time = st.time_input(
            "Task time"
        )

        frequency = st.selectbox(
            "Frequency",
            ["once", "daily", "weekly"]
        )

        add_task = st.form_submit_button("Add Task")

        if add_task:

            if not task_description.strip():
                st.warning("Please enter a task description.")

            else:
                selected_pet = next(
                    pet
                    for pet in st.session_state.owner.pets
                    if pet.name == selected_pet_name
                )

                new_task = Task(
                    description=task_description.strip(),
                    time=task_time.strftime("%H:%M"),
                    frequency=frequency
                )

                selected_pet.add_task(new_task)

                st.success(
                    f"{new_task.description} added for "
                    f"{selected_pet.name}!"
                )

else:
    st.info(
        "Save an owner and add at least one pet before adding tasks."
    )


# -------------------------
# CURRENT TASKS
# -------------------------

st.divider()
st.header("📋 Current Tasks")

if st.session_state.owner:

    scheduler = Scheduler(st.session_state.owner)

    task_rows = []

    for pet in st.session_state.owner.pets:
        for task in pet.get_tasks():
            task_rows.append(
                {
                    "Pet": pet.name,
                    "Task": task.description,
                    "Time": task.time,
                    "Frequency": task.frequency,
                    "Status": (
                        "Completed"
                        if task.completed
                        else "Pending"
                    )
                }
            )

    if task_rows:
        st.table(task_rows)
    else:
        st.info("No tasks have been added yet.")

else:
    st.info("No owner has been created yet.")


# -------------------------
# DAILY SCHEDULE
# -------------------------

st.divider()
st.header("📅 Daily Schedule")

if st.button("Generate Schedule"):

    if st.session_state.owner is None:
        st.warning("Please create an owner first.")

    else:
        scheduler = Scheduler(st.session_state.owner)

        tasks = scheduler.sort_by_time()

        if not tasks:
            st.warning(
                "Add at least one task before generating a schedule."
            )

        else:
            st.success("Today's Pet Care Schedule")

            conflicts = scheduler.detect_conflicts()

            if conflicts:
                for task1, task2 in conflicts:
                    st.warning(
                        f"Scheduling conflict: {task1.description} and "
                        f"{task2.description} are both scheduled at "
                        f"{task1.time}."
                    )

            for task in tasks:
                status = (
                    "✅ Completed"
                    if task.completed
                    else "⏳ Pending"
                )

                st.write(
                    f"**{task.time}** — "
                    f"{task.description} "
                    f"({task.frequency}) — "
                    f"{status}"
                )