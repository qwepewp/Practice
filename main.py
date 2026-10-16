"""Главный модуль консольного приложения 'Менеджер отчётов'."""

from file_utils import load_reports_from_file, save_reports_to_file
from reports import TextReport


def print_menu() -> None:
    """Выводит главные пункты меню."""
    print("\n=== МЕНЕДЖЕР ОТЧЁТОВ ===")
    print("1. Добавить текстовый отчёт")
    print("2. Посмотреть все отчёты и статистику")
    print("3. Сохранить отчёты в файл")
    print("4. Загрузить отчёты из файла")
    print("0. Выход")


def add_report_dialog(reports: list[TextReport]) -> None:
    """Диалог добавления нового отчёта с проверкой некорректного ввода."""
    title = input("Введите название отчёта: ").strip()
    if not title:
        print("Ошибка: Название не может быть пустым!")
        return

    print("Введите текст отчёта (для завершения наберите 'END' с новой строки):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    content = "\n".join(lines)
    try:
        new_rep = TextReport(title, content)
        reports.append(new_rep)
        print(f"Отчёт '{title}' успешно добавлен!")
    except ValueError as err:
        print(f"Ошибка валидации: {err}")


def show_reports(reports: list[TextReport]) -> None:
    """Показывает список всех отчётов в памяти."""
    if not reports:
        print("\nСписок отчётов пуст.")
        return

    print("\n--- Список всех отчётов ---")
    for idx, rep in enumerate(reports, 1):
        print(f"{idx}. {rep.summary()}")


def main() -> None:
    """Основной цикл программы."""
    reports: list[TextReport] = []

    while True:
        print_menu()
        choice = input("Выберите действие (0-4): ").strip()

        if choice == '1':
            add_report_dialog(reports)
        elif choice == '2':
            show_reports(reports)
        elif choice == '3':
            save_reports_to_file(reports)
        elif choice == '4':
            reports = load_reports_from_file()
        elif choice == '0':
            print("Работа программы завершена. До свидания!")
            break
        else:
            print("Некорректный ввод! Пожалуйста, введите цифру от 0 до 4.")


if __name__ == '__main__':
    main()