# 🏏 Computer vs You — Hand Cricket

A small **Python command-line Hand Cricket game** created as my **second Python project** while learning and revising Python.

This project was mainly built to practice Python fundamentals by actually creating something instead of only studying syntax and theory.

> 📌 **Project Status:** Beginner / Learning Project
> 🐍 **Language:** Python
> 📅 **Created during:** Day 4 of my Python revision

---

## 🎮 About the Project

This is a simple **Computer vs You Hand Cricket game**.

The player and computer choose numbers between `1` and `6`.

* If the batter's number matches the bowler's number → **Wicket**
* If the numbers are different → the batter scores runs
* A toss decides who bats or bowls first
* Both sides get an opportunity to bat
* The final scores are compared

The project also includes a basic scoreboard stored in a text file.

---

## 🧠 Why I Built This

This is my **second project after learning Python**.

Instead of trying to build a large or complicated application, I wanted to test whether I could combine basic Python concepts into one working program.

The project helped me practice:

* Functions
* Loops
* Conditional statements
* `input()`
* Type conversion
* Lists
* Dictionaries
* Random numbers
* File handling
* Returning values from functions
* Passing arguments between functions
* Basic program flow

---

# ⚠️ Important: This Project Has Issues

This project is **not production-quality code**.

I have intentionally kept the original version because it represents where I was during the early stages of learning Python.

There are several problems with the implementation.

### 1. Poor Code Architecture

The program has too many functions communicating with each other in a somewhat complicated way.

For example, the batting and bowling functions receive values such as:

```python
batt(t_run, bot_run)
```

but the way those values are passed around isn't well designed.

I now realize that the program would be much cleaner with a better overall architecture.

---

### 2. The I/O and File Handling Could Be Much Better

I implemented a simple `score.txt` file to save the scoreboard.

However, the file system implementation isn't particularly useful for this type of game.

For a small command-line game like this, the scoreboard could simply be maintained in memory and displayed directly.

If persistent data were actually required, the project would benefit from a more structured approach rather than simply overwriting a text file.

So, looking back, **implementing file I/O here wasn't necessarily a good design decision**.

---

### 3. Input Validation Is Weak

There are several places where invalid input can cause problems.

For example:

```python
run = int(input(...))
```

If the user enters:

```text
abc
```

the program will crash because `abc` cannot be converted to an integer.

A better implementation would use proper validation and exception handling.

---

### 4. The Game Logic Needs Improvement

Some of the cricket rules are simplified and don't perfectly represent proper Hand Cricket.

The No-Ball/Wide implementation is also somewhat inconsistent.

The computer can generate values such as `7` or `8` to represent special situations, which is not the cleanest way to design the game logic.

A better version would explicitly represent events such as:

```text
NORMAL BALL
NO BALL
WIDE
WICKET
```

instead of using numbers outside the normal range.

---

### 5. The Program Needs Better State Management

One of the biggest things I realized while making this project is that the game has **state**:

* Player score
* Computer score
* Current innings
* Batting side
* Bowling side
* Number of balls
* Wicket status
* Target score

Managing all of this using separate variables and function arguments quickly becomes messy.

This is one of the reasons I realized that **OOP (Object-Oriented Programming)** would be useful for a project like this.

---

# 💡 My Biggest Realization

While building this project, I realized that knowing Python syntax is very different from knowing how to **design a Python program**.

I can write:

```python
if
while
for
def
input()
random
```

but combining them into a clean, scalable application requires a different level of understanding.

This project made me realize that I need to improve my understanding of:

* OOP
* Classes and objects
* State management
* Exception handling
* Better program architecture
* Modular programming
* Clean code
* Data structures
* Testing

---

# 📚 What I Learned From This Project

The most important thing I learned wasn't actually the Hand Cricket game.

It was realizing **what I don't know yet**.

While writing this project, I started noticing questions such as:

> "Where should this variable actually live?"

> "Why am I passing the same variables through so many functions?"

> "Would a class make this easier?"

> "Should this data really be stored in a file?"

> "What happens if the user enters something unexpected?"

These are things that I probably wouldn't have noticed by only watching Python tutorials.

Building the project exposed these gaps.

---

# 🗓️ My Python Learning Journey

This project was created on approximately **Day 4 of revising Python**.

I am still very early in the learning process.

My goal at this stage isn't to write perfect code.

My goal is to:

**Learn → Build → Break → Understand → Improve**

This project is one of the first steps in that process.

---

# 🔧 What I Would Change in Version 2

If I rebuild this project after learning more Python, I would like to:

* [ ] Rewrite the game architecture
* [ ] Use OOP where appropriate
* [ ] Create proper `Player` / `Game` classes
* [ ] Improve input validation
* [ ] Add exception handling
* [ ] Remove unnecessary file I/O
* [ ] Properly manage game state
* [ ] Separate game logic from user interface
* [ ] Create cleaner functions
* [ ] Improve the innings system
* [ ] Implement proper target chasing
* [ ] Improve No-Ball/Wide logic
* [ ] Add proper winner/loser handling
* [ ] Add replay functionality
* [ ] Add automated tests

---

# 📂 Current Project Structure

```text
Hand-Cricket/
│
├── hand_cricket.py
├── score.txt
└── README.md
```

The current structure is intentionally simple because this is an early learning project.

---

# 🚀 Future Version

I don't consider this project finished from a programming perspective.

The current version is more like a **snapshot of my learning progress**.

After learning more advanced Python concepts, especially **OOP and better software design**, I would like to come back to this project and rebuild it properly.

That would allow me to compare:

**Version 1:**
*"I know Python syntax and can build something."*

vs.

**Version 2:**
*"I understand how to design a Python application."*

---

## 👨‍💻 Final Note

This is only my **second Python project**, and I am currently on **Day 4 of revising Python**.

So yes, the code has issues. 😅

But that's exactly why I am keeping it.

A project doesn't have to be perfect to be valuable.

For me, this project was important because it showed me that **building software is more than knowing syntax — it's about thinking about structure, logic, data, and maintainability.**

This is the beginning of my Python journey, not the final version.

**Build. Break. Learn. Improve. 🚀🐍**
