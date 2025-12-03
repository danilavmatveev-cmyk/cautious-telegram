# fix_turtle.py - исправление путей для turtle
import os
import sys


def fix_tkinter_paths():
    """Исправляет пути для Tkinter при работе с кириллическими именами пользователей"""
    if sys.platform == 'win32':
        # Путь к Python (может потребоваться изменить)
        python_paths = [
            r'C:\Users\Д\AppData\Local\Programs\Python\Python313',
            # Добавьте другие возможные пути при необходимости
        ]

        for python_dir in python_paths:
            tcl_path = os.path.join(python_dir, 'tcl', 'tcl8.6')
            tk_path = os.path.join(python_dir, 'tcl', 'tk8.6')

            if os.path.exists(tcl_path) and os.path.exists(tk_path):
                os.environ['TCL_LIBRARY'] = tcl_path
                os.environ['TK_LIBRARY'] = tk_path
                print(f"Исправлены пути Tcl/Tk: {tcl_path}")
                return True

        print("Не удалось найти Tcl/Tk библиотеки. Проверьте установку Python.")
        return False


# Автоматически исправляем при импорте
fix_tkinter_paths()