import os
import shutil
import sys

def copy_files_recursively(source_dir, dest_dir):
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            # Рекурсивно обробляємо піддиректорії
            copy_files_recursively(item_path, dest_dir)
        else:
            # Визначаємо розширення файлу і створюємо відповідну піддиректорію в директорії призначення
            file_extension = os.path.splitext(item)[1][1:]  # Видаляємо крапку з розширення
            if file_extension == '':
                file_extension = 'no_extension'
            extension_dir = os.path.join(dest_dir, file_extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)
            # Копіюємо файл у нову директорію
            shutil.copy2(item_path, extension_dir)

if __name__ == "__main__":
    # Перевіряємо аргументи командного рядка
    if len(sys.argv) < 2:
        print("Usage: python task_1.py source_dir [dest_dir]")
        sys.exit(1)
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    try:
        copy_files_recursively(source_dir, dest_dir)
    except Exception as e:
        print(f"Error: {e}")
