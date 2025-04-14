import argparse
import os
import sys
from multiprocessing import Pool
from report_registry import get_report
from utils.parser import parse_log_file

def process_file(file_path):
    return parse_log_file(file_path)

def merge_results(results):
    merged = {}
    for result in results:
        for path, levels in result.items():
            if path not in merged:
                merged[path] = {lvl: 0 for lvl in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]}
            for lvl, count in levels.items():
                merged[path][lvl] += count
    return merged

def main():
    parser = argparse.ArgumentParser(description="Log analyzer CLI")
    parser.add_argument("log_files", nargs='+', help="Paths to log files")
    parser.add_argument("--report", required=True, help="Report type (e.g. handlers)")
    args = parser.parse_args()

    for path in args.log_files:
        if not os.path.isfile(path):
            print(f"Log file not found: {path}", file=sys.stderr)
            sys.exit(1)

    report_fn = get_report(args.report)
    if report_fn is None:
        print(f"Unknown report type: {args.report}", file=sys.stderr)
        sys.exit(1)

    with Pool() as pool:
        parsed_results = pool.map(process_file, args.log_files)

    merged_data = merge_results(parsed_results)
    print("
Report:")
    report_fn(merged_data)

if __name__ == "__main__":
    main()
