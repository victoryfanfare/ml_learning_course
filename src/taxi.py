"""Небольшие аналитические запросы к данным такси."""

from src.db import query_df


def top_routes(n: int = 10):
    """Вернуть n самых частых маршрутов между разными известными районами.

    Исключаем поездки с неположительными расстоянием, чеком или временем.
    n передаётся параметром ClickHouse, а не вставляется в SQL строкой.
    """
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 50:
        raise ValueError("n должно быть целым числом от 1 до 50")

    return query_df(
        """
        SELECT
            pickup_ntaname AS pickup_area,
            dropoff_ntaname AS dropoff_area,
            count() AS trips,
            round(avg(total_amount), 2) AS avg_total
        FROM nyc_taxi.trips_small
        WHERE notEmpty(trimBoth(pickup_ntaname))
          AND notEmpty(trimBoth(dropoff_ntaname))
          AND pickup_ntaname != dropoff_ntaname
          AND trip_distance > 0
          AND total_amount > 0
          AND dropoff_datetime > pickup_datetime
        GROUP BY pickup_ntaname, dropoff_ntaname
        ORDER BY trips DESC, pickup_area, dropoff_area
        LIMIT {n:UInt32}
        """,
        parameters={"n": n},
    )
