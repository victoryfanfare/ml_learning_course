"""Подключение к ClickHouse.

Параметры берутся из файла .env, а не пишутся в ноутбуке.
Так пароль не попадёт ни в git, ни в вывод ячейки, ни в скриншот в чате.

Использование:

    from src.db import get_client, query_df

    client = get_client()
    df = query_df("SELECT * FROM nyc_taxi.trips_small LIMIT 10")
"""

import os
from functools import lru_cache

import clickhouse_connect
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def _required(name: str) -> str:
    """Достаёт переменную окружения и внятно ругается, если её нет."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Не задана переменная {name}. "
            "Проверьте: файл .env существует (cp .env.example .env) "
            "и переменная в нём заполнена."
        )
    return value


@lru_cache(maxsize=1)
def get_client():
    """Возвращает клиент ClickHouse. Соединение создаётся один раз за сессию."""
    return clickhouse_connect.get_client(
        host=_required("CLICKHOUSE_HOST"),
        port=int(os.getenv("CLICKHOUSE_PORT", "8443")),
        username=_required("CLICKHOUSE_USER"),
        # пароль может быть пустым: у публичного пользователя demo его нет
        password=os.getenv("CLICKHOUSE_PASSWORD", ""),
        database=os.getenv("CLICKHOUSE_DATABASE", "default"),
        secure=os.getenv("CLICKHOUSE_SECURE", "true").lower() == "true",
    )


def query_df(sql: str, parameters: dict | None = None) -> pd.DataFrame:
    """Выполняет запрос и отдаёт результат сразу в виде DataFrame."""
    return get_client().query_df(sql, parameters=parameters)
