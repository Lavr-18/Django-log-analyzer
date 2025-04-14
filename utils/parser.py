
import re
from typing import Dict

LOG_PATTERN = re.compile(
    r'(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL).*?"GET (?P<path>/[^"]*)"'
)

def parse_log_file(file_path: str) -> Dict[str, Dict[str, int]]:
    result = {}
    with open(file_path, 'r') as f:
        for line in f:
            match = LOG_PATTERN.search(line)
            if match:
                path = match.group("path")
                level = match.group("level")
                if path not in result:
                    result[path] = {lvl: 0 for lvl in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]}
                result[path][level] += 1
    return result
