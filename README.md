# Command Line Interface 📋 

A command-line tool for managing your to-do tasks. Easily create, view, complete, and edit tasks directly from your terminal!

## 🚀 Features

- **Create Tasks**: Add new tasks with a unique ID.
- **View Tasks**: Display all tasks in a neat tabular format.
- **Complete Tasks**: Mark tasks as completed by removing them from the list.
- **Edit Tasks**: Update the title, description, and due date of existing tasks.

## 🛠️ Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
2. Install  the required packages:
   ```sh
    pip install -r requirements.txt

   
## 💻 How to run Command Line Interface
1. Run the CLI:
    ```
    python app.py
2. Create a Task:
    ```
    python app.py add --create "Title,Description,2024-05-20"
    
  Example:
    ```
    
    python app.py add --create "Buy groceries,Buy milk and bread,2024-05-20"
    
3. Show All Tasks:
    ```
    python app.py show
    
4. Complete a Task:
    ```
    python app.py complete --taskid 1
    
5. Edit a Task:
    ```
    python app.py edit --taskid 1
You will be prompted to update the title, description, and due date interactively.
   
   
