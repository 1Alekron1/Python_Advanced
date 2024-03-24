import json
from collections import Counter
from datetime import datetime

# Чтение логов из файла и десериализация JSON
with open('skillbox_json_messages.log', 'r') as file:
    logs = [json.loads(line) for line in file]

# Подзадача 1: Сколько было сообщений каждого уровня за сутки
levels_count = Counter(log['level'] for log in logs)

# Подзадача 2: В какой час было больше всего логов
hour_counts = Counter(datetime.strptime(log['time'], '%Y-%m-%d %H:%M:%S,%f').hour for log in logs)
most_common_hour = max(hour_counts, key=hour_counts.get)

# Подзадача 3: Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00
critical_logs_count = sum(1 for log in logs if log['level'] == 'CRITICAL' and '05:00:00' <= log['time'] <= '05:20:00')

# Подзадача 4: Сколько сообщений содержат слово dog
dog_messages_count = sum(1 for log in logs if 'dog' in log['message'].lower())

# Подзадача 5: Какое слово чаще всего встречалось в сообщениях уровня WARNING
warning_messages = [log['message'].lower() for log in logs if log['level'] == 'WARNING']
word_counts = Counter(word for message in warning_messages for word in message.split())
most_common_word = max(word_counts, key=word_counts.get)

# Вывод результатов
print("1. Сколько было сообщений каждого уровня за сутки:", levels_count)
print("2. В какой час было больше всего логов:", most_common_hour)
print("3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00:", critical_logs_count)
print("4. Сколько сообщений содержат слово dog:", dog_messages_count)
print("5. Какое слово чаще всего встречалось в сообщениях уровня WARNING:", most_common_word)
