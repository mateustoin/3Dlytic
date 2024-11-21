# 3Dlytic
3D Printing software to help you with pricing and simple reports analytics for 3D prints!

---

## 🔧 Features
- Simple graphical user interface created with Qt Designer.
- Separation of logic (Model), interface (View), and control (Controller) using the MVC pattern.
- Cross-platform compatibility.
- Customizable styling through a QSS file.

## 🛠️ Technologies Used

- Language: Python 3.8+.
- Framework: PyQt5 (or PySide6, depending on your preference).
- Interface: .ui file generated with Qt Designer.

## ⚙️ Requirements

### Required Software
- Python 3.8 or newer.
- Pip (Python package manager).
- Qt Designer (optional, for editing the .ui file).

### Installing Dependencies
Install the required dependencies with the following command:

```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Generate the Python File from .ui

If you modify the views/main_view.ui file, regenerate the corresponding Python file using:

```bash
pyside6-uic -o views/main_view.py views/main_view.ui
```
## 📦 Deployment

TODO: Create executable instructions.

## 🤝 Contributing

1. Fork this repository.
2. Create your feature branch:
```bash
git checkout -b feature/new-feature
```
3. Commit your changes:
```bash
git commit -m 'Added a new feature'
```
4. Push to the branch:
```bash
git push origin feature/new-feature
```
5. Open a Pull Request.