# Django Log Analyzer CLI

CLI-приложение для анализа логов Django и формирования отчётов.

## Установка и запуск

```bash
python3 main.py path/to/log1.log path/to/log2.log --report handlers
```

## Пример отчёта

```
Report:
HANDLER               	DEBUG  	INFO   	WARNING	ERROR  	CRITICAL
/api/v1/test/         	1      	2      	0      	1      	0

                        1      	2      	0      	1      	0

Total requests: 4
```

## Доступные отчёты

- `handlers` — отчёт о количестве запросов к каждой ручке по уровням логирования.

## Тесты

```bash
pytest
```
