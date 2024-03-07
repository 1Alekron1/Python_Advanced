from typing import List, Optional


def get_mean_size(file_info: str) -> Optional[float]:
    lines: List[str] = file_info.split('\n')[1:]
    file_sizes: List[int] = []

    for line in lines:
        tokens: List[str] = line.split()
        if len(tokens) >= 5:
            file_size: str = tokens[4]
            try:
                file_sizes.append(int(file_size))
            except ValueError:
                continue

    if file_sizes:
        return sum(file_sizes) / len(file_sizes)
    else:
        return None


if __name__ == "__main__":
    import sys

    data: str = sys.stdin.read()
    mean_size: Optional[float] = get_mean_size(data)
    if mean_size is not None:
        print(mean_size)
    else:
        print("No files found or unable to determine file sizes.")
