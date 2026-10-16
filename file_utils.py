"""Модуль для безопасной работы с файловой системой."""

from reports import TextReport, log_call

DEFAULT_FILE = 'reports.txt'


@log_call
def save_reports_to_file(reports: list[TextReport], filename: str = DEFAULT_FILE) -> None:
    """Сохраняет список отчётов в файл."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for rep in reports:
                # Экранируем переносы в содержимом для удобного хранения
                safe_content = rep.content.replace('\n', '\\n')
                f.write(f"{rep.title}|{safe_content}\n")
        print(f"Успешно сохранено отчётов: {len(reports)}")
    except PermissionError:
        print("Ошибка: Нет прав для записи в файл!")
    except OSError as e:
        print(f"Ошибка файловой системы при сохранении: {e}")


@log_call
def load_reports_from_file(filename: str = DEFAULT_FILE) -> list[TextReport]:
    """Загружает список отчётов из файла."""
    loaded_reports = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split('|', 1)
                if len(parts) == 2:
                    title, raw_content = parts
                    content = raw_content.replace('\\n', '\n')
                    loaded_reports.append(TextReport(title, content))
        print(f"Загружено отчётов из файла: {len(loaded_reports)}")
    except FileNotFoundError:
        print("Файл с отчётами пока не создан. Будет создан новый при сохранении.")
    except PermissionError:
        print("Ошибка: Нет прав на чтение файла!")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return loaded_reports