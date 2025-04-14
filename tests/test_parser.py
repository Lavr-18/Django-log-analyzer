
from utils.parser import parse_log_file
import tempfile

def test_parse_log_file():
    log_data = """INFO 2024-04-12 django.request "GET /api/v1/test/" 200
DEBUG 2024-04-12 django.request "GET /api/v1/test/" 200
ERROR 2024-04-12 django.request "GET /api/v1/test/" 500
"""
    with tempfile.NamedTemporaryFile("w+", delete=False) as f:
        f.write(log_data)
        f.flush()
        result = parse_log_file(f.name)

    assert result["/api/v1/test/"]["INFO"] == 1
    assert result["/api/v1/test/"]["DEBUG"] == 1
    assert result["/api/v1/test/"]["ERROR"] == 1
