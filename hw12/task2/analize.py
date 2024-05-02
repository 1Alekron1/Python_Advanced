import subprocess

def process_count(username: str) -> int:
    ps_command = f"ps -u {username} -o pid= | wc -l"
    ps_process = subprocess.Popen(ps_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ps_output, ps_error = ps_process.communicate()
    if ps_process.returncode == 0:
        return int(ps_output.strip())
    else:
        print(f"Error: {ps_error.decode()}")
        return -1

def total_memory_usage(root_pid: int) -> float:
    rss_command = f"ps --ppid {root_pid} -o rss= | awk '{{sum+=$1}} END {{print sum}}'"
    rss_process = subprocess.Popen(rss_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rss_output, rss_error = rss_process.communicate()
    if rss_process.returncode == 0:
        total_memory = int(rss_output.strip())
        return total_memory / (1024 * 1024)  # Convert to MB
    else:
        print(f"Error: {rss_error.decode()}")
        return -1
