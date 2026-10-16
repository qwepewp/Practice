"""Модуль с классами отчётов и декораторами."""

import time
from functools import wraps


def log_call(func):
    """Декоратор для логирования вызова функции и замера времени."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Запуск операции: {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[LOG] Завершено за {duration:.4f} сек.")
        return result
    return wrapper


class Report:
    """Базовый класс отчёта."""

    def __init__(self, title: str, content: str):
        if not title.strip():
            raise ValueError("Название отчёта не может быть пустым.")
        self._title = title.strip()
        self._content = content

    @property
    def title(self) -> str:
        return self._title

    @property
    def content(self) -> str:
        return self._content

    def summary(self) -> str:
        """Возвращает краткую сводку по отчёту."""
        return f"Отчёт '{self._title}': {len(self._content)} символов"

    def __str__(self) -> str:
        return f"Report('{self._title}')"


class TextReport(Report):
    """Класс-наследник для текстовых отчётов."""

    def summary(self) -> str:
        """Переопределённый метод сводки с подсчётом слов."""
        words_count = len(self._content.split())
        lines_count = len(self._content.splitlines()) if self._content else 0
        return (
            f"[Текстовый отчёт] '{self._title}': "
            f"{lines_count} стр., {words_count} слов, {len(self._content)} симв."
        )
    