from pydantic_settings import BaseSettings, SettingsConfigDict

import locust.stats

# Импортируем вложенные модели
from tools.config.grpc import GRPCClientConfig
from tools.config.http import HTTPClientConfig
from tools.config.locust import LocustUserConfig

locust.stats.PERCENTILES_TO_REPORT = [0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99, 1.0]
locust.stats.CSV_STATS_INTERVAL_SEC = 5
locust.stats.HISTORY_STATS_INTERVAL_SEC = 5
locust.stats.CONSOLE_STATS_INTERVAL_SEC = 5
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 5


# Для каждого окружения заводим свой файл:
# .env.local
# .env.dev
# .env.test
# .env.stage
# (иногда ещё prod)

class Settings(BaseSettings):
    # Конфигурация загрузки — откуда брать переменные
    model_config = SettingsConfigDict(
        extra="allow",  # Разрешить дополнительные поля (например, неиспользуемые переменные)
        env_file=".env.local",  # Указываем имя основного .env файла
        # env_file=f".env.{os.getenv('ENV', 'local')}",  # по умолчанию .env.local
        env_file_encoding="utf-8",  # Кодировка файла
        env_nested_delimiter="."  # Позволяет использовать вложенные переменные, например: LOCUST_USER.WAIT_TIME_MIN
    )

    # Теперь можно запускать нагрузочные тесты с нужной конфигурацией:
    # ENV=dev locust
    # ENV=test locust
    # ENV=stage locust
    # Pydantic автоматически подгрузит .env.dev, .env.test или .env.stage.

    # Вложенные секции настроек
    locust_user: LocustUserConfig  # Настройки виртуального пользователя
    gateway_http_client: HTTPClientConfig  # Настройки HTTP-клиента
    gateway_grpc_client: GRPCClientConfig  # Настройки gRPC-клиента


# Глобальный объект настроек — его можно импортировать в любом месте проекта
settings = Settings()
