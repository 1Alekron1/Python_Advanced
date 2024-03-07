from typing import List


def get_summary_rss(file_path: str) -> str:
    with open(file_path, 'r') as file:
        lines: List[str] = file.readlines()[1:]

    total_bytes: int = 0

    for line in lines:
        columns: List[str] = line.split()
        rss: int = int(columns[5])
        total_bytes += rss

    def format_bytes(bytes_: int) -> str:
        for unit in ['Б', 'Кб', 'Мб', 'Гб']:
            if bytes_ < 1024:
                return f"{bytes_} {unit}"
            bytes_ /= 1024
        return f"{bytes_} Тб"

    return format_bytes(total_bytes)


if __name__ == "__main__":
    file_path: str = "../output_file.txt"
    print(get_summary_rss(file_path))
