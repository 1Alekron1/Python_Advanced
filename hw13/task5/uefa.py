import sqlite3
import random

other_commands = ('Bulls USA, Heat USA, Lakers USA, Celtics USA, Raptors Canada, Rockets USA, 76ers USA, Nuggets USA, '
                  'Mavericks USA, Nets USA, Warriors USA, Trail Blazers USA, Spurs USA, Jazz USA, Thunder USA, '
                  'Pacers USA, Suns USA, Grizzlies USA, Pelicans USA, Hawks USA, Wizards USA, Timberwolves USA, '
                  'Hornets USA, Magic USA, Pistons USA, Kings USA, Real Madrid Spain, Barcelona Spain, Atletico Madrid Spain, '
                  'Valencia Spain, Sevilla Spain, Bayern Munich Germany, Borussia Dortmund Germany, RB Leipzig Germany, '
                  'PSG France, Marseille France, Lyon France, Juventus Italy, Inter Milan Italy, AC Milan Italy, Napoli Italy, '
                  'Roma Italy, Ajax Netherlands, PSV Eindhoven Netherlands, Feyenoord Netherlands, Benfica Portugal, Porto Portugal, '
                  'Sporting Lisbon Portugal, Galatasaray Turkey, Fenerbahce Turkey, Besiktas Turkey, Celtic Scotland, '
                  'Rangers Scotland, Porto Portugal, Porto Portugal, Celtic Scotland, Rangers Scotland, Boca Juniors Argentina, '
                  'River Plate Argentina, Sao Paulo Brazil, Flamengo Brazil, Corinthians Brazil, Palmeiras Brazil, '
                  'Vasco da Gama Brazil, Santos Brazil, Atletico Mineiro Brazil, Internacional Brazil, Gremio Brazil, '
                  'Fluminense Brazil, Botafogo Brazil, Cruzeiro Brazil, Pachuca Mexico, Tigres Mexico, Monterrey Mexico, '
                  'Chivas Mexico, Club America Mexico, Santos Laguna Mexico, Cruz Azul Mexico, Leon Mexico, Necaxa Mexico, Puebla Mexico')
other_commands_list = other_commands.split(", ")

sql_insert_uefa_commands = """INSERT INTO 'uefa_commands' 
(command_number, command_name, command_country, command_level) VALUES (?, ?, ?, ?)
"""

sql_insert_uefa_draw = """INSERT INTO 'uefa_draw' (command_number, group_number) VALUES (?, ?)
"""


def generate_test_data(cursor: sqlite3.Cursor, number_of_groups: int) -> None:
    command_levels = [number_of_groups, number_of_groups * 2, number_of_groups]
    command_levels_group = [[1, 2, 1] for _ in range(number_of_groups)]
    command_data = []
    draw_data = []

    for i in range(1, number_of_groups * 4 + 1):
        command = random.choice(other_commands_list).split()
        level = int(random.choice(["1", "2", "3"]))

        while command_levels[level - 1] == 0:
            level = int(random.choice(["1", "2", "3"]))

        group_index = level - 1
        group_count = 0

        while command_levels_group[group_count][group_index] == 0:
            group_count += 1
        else:
            command_levels_group[group_count][group_index] -= 1
            draw_data.append((i, group_count + 1))

        command_levels[level - 1] -= 1
        command_data.append((i, command[0], command[1], level))

    cursor.executemany(sql_insert_uefa_commands, command_data)
    cursor.executemany(sql_insert_uefa_draw, draw_data)


if __name__ == "__main__":
    with sqlite3.connect("../homework.db") as conn:
        cursor = conn.cursor()
        number_of_groups = int(input("Enter the number of groups:\n"))
        generate_test_data(cursor, number_of_groups)
