# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial design for PawPal+ uses four main classes: Owner, Pet, Task, and Scheduler. The goal is to keep each class responsible for a specific part of the pet care management system.

The three core actions a user should be able to perform are:

1. Add and manage multiple pets.
2. Schedule tasks such as feeding, walking, medication, and appointments for a pet.
3. View and manage a daily schedule, including marking tasks as completed.

The classes and their responsibilities are:

- **Owner:** Stores the owner's information and manages multiple pets. It will also provide access to tasks from all of the owner's pets.
- **Pet:** Stores information about an individual pet and manages the tasks assigned to that pet.
- **Task:** Represents a pet care activity. It stores information such as the task description, time, frequency, and completion status.
- **Scheduler:** Retrieves tasks through the Owner and organizes them across multiple pets. It will be responsible for functionality such as sorting, filtering, recurring tasks, and detecting scheduling conflicts.

The main relationships in my design are that one Owner can have multiple Pets, each Pet can have multiple Tasks, and the Scheduler works with the Owner to access and organize tasks across all pets.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
