
from typing import Dict

def generate_handlers_report(data: Dict[str, Dict[str, int]]) -> None:
    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    total_by_level = {level: 0 for level in levels}
    total_requests = 0

    print("HANDLER                	" + "	".join(levels))

    for handler in sorted(data.keys()):
        line = f"{handler:<24}"
        for level in levels:
            count = data[handler].get(level, 0)
            line += f"	{count:<7}"
            total_by_level[level] += count
            total_requests += count
        print(line)

    total_line = " " * 24
    for level in levels:
        total_line += f"	{total_by_level[level]:<7}"
    print(total_line)
    print(f"\nTotal requests: {total_requests}")
