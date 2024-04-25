# To-Do List GUI Application

This is a Python-based To-Do List application with a Graphical User Interface (GUI) built using Tkinter library. It allows users to add, edit, delete, mark as completed/uncompleted, and clear tasks.

## Features

- **Add Task**: Users can add a new task by entering the task description.
- **Edit Task**: Users can edit existing tasks by selecting the task and providing a new description.
- **Delete Task**: Users can delete tasks either individually or clear all tasks at once.
- **Complete Task**: Users can mark a task as completed, moving it to the completed task list.
- **Uncomplete Task**: Users can revert a completed task back to the main task list.
- **Save and Load**: Tasks are saved to a file (`tasks.txt`) upon modification and loaded at application startup.

## Dependencies

This application requires Python 3.x and the following libraries:
- `tkinter`: For creating the GUI.
- `simpledialog`, `messagebox`: For displaying dialogs and gathering user input.

## Usage

1. Run the script (`todo_list.py`) using Python.
2. Upon running, the GUI window will appear.
3. Perform the desired actions:
   - Click "Add Task" to add a new task.
   - Select a task and click "Edit Task" to modify it.
   - Select a task and click "Delete Task" to remove it.
   - Click "Complete Task" to mark a task as completed.
   - Click "Uncomplete Task" to revert a completed task.
   - Click "Clear All" to remove all tasks.
4. Tasks are automatically saved to `tasks.txt` upon any modification.
5. Close the application window to exit.

## File Structure

- `todo_list.py`: The main Python script containing the application logic.
- `tasks.txt`: A text file used to store the tasks.

## Screenshot
![Screenshort of the program]([image_url](https://github.com/meetvivek/CODEWAY/blob/63800f174b799ca7630b9cb0dd5a6b7b0a2ed9e6/To-Do%20List%20application/screenshot.png))

## Contributions

Contributions to this project are welcome! If you would like to contribute, feel free to fork this repository, make your changes, and submit a pull request. Please ensure that your contributions align with the goals and guidelines of this project.

## Additional Notes

- The GUI design utilizes images for buttons and a background image for aesthetic purposes. Ensure that the image files are placed in the correct directory (`./icons/`).
- Ensure proper file permissions for read/write operations to `tasks.txt`.
- This project can be further extended by adding features such as task prioritization, due dates, and user authentication.
