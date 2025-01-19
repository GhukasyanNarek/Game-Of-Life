# 🌟 Conway's Game of Life

## 📝 Description
Conway's Game of Life is a cellular automaton created by John Horton Conway. This Python implementation generates and simulates grid-based patterns directly in the terminal, evolving dynamically over generations based on predefined rules. The game demonstrates the emergence of complex behaviors from simple rules.

---

### 🌍 Rules of Conway's Game of Life
1. **Survival**: A live cell with 2 or 3 neighbors stays alive to the next generation.
2. **Underpopulation**: A live cell with fewer than 2 neighbors dies.
3. **Overpopulation**: A live cell with more than 3 neighbors dies.
4. **Reproduction**: A dead cell with exactly 3 neighbors becomes a live cell.

---

### 📷 Visual Representation
Below is an example of the program's output in the terminal, where white blocks represent live cells and black spaces represent dead cells:

![Conway's Game of Life Terminal Representation](https://github.com/user-attachments/assets/c2e84414-9ec1-4a2b-8bbe-42429665a858)


---

## 🛠 Prerequisites

### 💻 System Requirements
- **Operating System:** macOS, Windows, or Linux
- **Python Version:** Python 3.8 or newer

---

## 🚀 Setup and Usage

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/GhukasyanNarek/Game-Of-Life/
```

### Step 2: Change Directory
Navigate to the directory where the repository was cloned:
```bash
cd Game-Of-Life
```

### Step 3: Run the Program
Run the program using Python:

#### On macOS and Linux:
```bash
python3 main.py
```

#### On Windows:
```bash
python main.py
```

---

### Step 4: Customize the Grid 
To modify grid size, generation speed, or initial patterns:
1. Open the `main.py` file in a text editor.
2. Adjust the following variables:
   - `GRID_SIZE`: Change the grid dimensions (e.g., `GRID_SIZE = (30, 30)` for a 30x30 grid).
   - `TIME_DELAY`: Set the time delay (in seconds) between generations (e.g., `TIME_DELAY = 0.5`).
   - `INITIAL_STATE`: Define custom starting patterns by specifying the coordinates of live cells (e.g., `INITIAL_STATE = [(3, 3), (3, 4), (3, 5)]`).

---

### 🧩 Features
- **Dynamic Simulation**: Observe grid evolution directly in the terminal with live updates.
- **Custom Patterns**: Experiment with different starting configurations and grid sizes.
- **Lightweight**: Runs entirely in the terminal without any external libraries.

---

### 🤝 Contributions
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---
