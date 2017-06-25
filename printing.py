from reports import *

FILENAME = 'game_stat.txt'
DECIDE_YEAR = 2000
GENRE = 'RPG'
TITLE = 'Counter-Strike'
print('number of games in file: ', count_games(FILENAME))
print('is there a game from year', DECIDE_YEAR, '?', decide(FILENAME, DECIDE_YEAR))
print('latest game in this list is: ', get_latest(FILENAME))
print('number of games that match genre -', GENRE, ':', count_by_genre(FILENAME, GENRE))
print('line number of game', TITLE, ':', get_line_number_by_title(FILENAME, TITLE))
print('sorted list: ', sort_abc(FILENAME))
print('sorted genre list: ', get_genres(FILENAME))
print('The top FPS was released in: ', when_was_top_sold_fps(FILENAME))
