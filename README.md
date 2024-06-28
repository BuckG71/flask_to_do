# Flask To-Do Application

This is a simple Flask To-Do application that allows users to add, update, delete, and view tasks. The application uses Tailwind CSS for styling.

## Features

- **Add Tasks**: Users can add new tasks.
- **View Tasks**: Users can view all tasks in a list.
- **Update Tasks**: Users can update existing tasks.
- **Delete Tasks**: Users can delete tasks.
- **Tailwind CSS**: The application is styled using Tailwind CSS.

## Project Structure

```
your_project/
├── src/
│   └── tailwind.css
├── static/
│   └── css/
│       └── tailwind.css
├── templates/
│   ├── base.html
│   ├── tasks.html
│   ├── add_task.html
│   ├── update_task.html
│   └── static_index.html
├── app.py
├── init_db.py
├── check_tables.py
├── tailwind.config.js
├── package.json
├── package-lock.json
├── tasks.db
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    cd flask_to_do
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Tailwind CSS**:
    ```bash
    npm install
    ```

5. **Build Tailwind CSS**:
    ```bash
    npm run build:css
    ```

6. **Initialize the database**:
    ```bash
    python init_db.py
    ```

7. **Run the Flask application**:
    ```bash
    flask run
    ```

8. **Open your browser**:
    Navigate to `http://127.0.0.1:5000/` to use the application.

## License

This project is licensed under the MIT License.