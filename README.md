# ⚡ Smurf CLI Task Manager

A lightweight, customized command-line interface task manager built because I can! 🤷‍♀️ It manages daily schedules, helps organize tasks cleanly, and stores everything locally in a secure, ignored data structure.

May have some bugs iono about so...help out🤷‍♀️

Help out in the GUI or frontend or UI/UX too if you wish, not at that level yet 🐧

Inspired by SuperProductivity :-), you can find them @:

https://github.com/super-productivity/super-productivity


---

## 🔒 Security & Privacy

Your data belongs to you. This application uses a local `DB.json` (was trying to emmulate postgreSQL) file to store all tasks, notes, and schedules. 
* **Zero Cloud Tracking:** No external APIs, third-party databases, or cloud servers are used. Everything stays on your local machine.
* **Git Shielded:** The repository includes a pre-configured `.gitignore` file that explicitly blocks your data from being accidentally pushed online or shared publicly.

---

## 🚀 Features

* **Add Tasks:** Quickly push tasks with custom titles, timings, and full descriptions.
* **Intelligent Search:** Scan through your database effortlessly with custom query matching.
* **Safe Deletion:** Interactive delete confirmation prompts so you never accidentally drop a task.
* **Local Storage:** Clean JSON tracking system that handles state persistent data storage across sessions.

---

## 🛠️ Setup & Installation

Make sure you have Python installed on your machine. Then, clone the repository and run the application:

```bash/zsh
# Clone this masterpiece
git clone [https://github.com/luvhendrixx/Smurf.git](https://github.com/luvhendrixx/Smurf.git)

# Jump into the directory
cd Smurf

# Fire up the engine!
python todo.py