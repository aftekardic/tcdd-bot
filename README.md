# TCDD BOT


TCDD BOT is an application designed to assist users in finding TCDD tickets and sending email notifications. As of now, the application supports one rotation.

## Getting Started

### Usage & Development

1. **Create a Virtual Environment:**
```
python -m venv env
```
2. **Activate the Virtual Environment:**
- **Linux/Mac:**
  ```
  cd /env/bin/
  source activate
  ```
- **Windows:**
  ```
  cd /env/Scripts
  activate
  ```

3. **Navigate to the Main Folder:**
```
cd ../../
```
4. **Install Dependencies:**
```
pip install -r requirements.txt
```
5. **Running:**
1. With terminal:
```
python main.py
```
2. Create an exe or app:
```
pyinstaller --noconfirm --onefile --windowed --hidden-import "PyQt5.QtWidgets" --hidden-import "PyQt5.QtCore" --hidden-import "PyQt5.QtGui" --hidden-import "ui" --hidden-import "datetime" --hidden-import "rpa" --hidden-import "custom_tools" src/main.py
```
   - After create an app/exe, your application is in the dist folder.

## Technologies Used
###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="Python"/>
  <img src="https://cdn.simpleicons.org/selenium/43B02A" height="40" alt="Selenium"  />
</div>

###

