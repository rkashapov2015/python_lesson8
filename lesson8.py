import os
import mmap

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
migration_path = os.path.join(current_dir, migrations)

keepGoing = True

def find_from_file(file_path, needed_word):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if needed_word in line:
                    return True
        return False
    except UnicodeError:
        return False

print(f"Абсолютный путь: {migration_path}")

while (keepGoing):
    try: 
        needed_words = input('Enter needed word: ')
        if not needed_words:
            keepGoing = False
            continue

        list_files = os.listdir(migration_path)
        number_files = 0
        for file_name in list_files:
            file_path = os.path.join(migration_path, file_name)
            if find_from_file(file_path, needed_words):
                print(file_name)
                number_files += 1
        print(f"Количество файлов {number_files}")
    except KeyboardInterrupt:
        keepGoing = False
