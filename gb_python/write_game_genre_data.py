# written by Mobolaji Williams,
# AC209-Final Proj

# This code writes the game genre data to a stable file. 
# Date and time of writing: 12/5/2014 11:52 PM

## DO NOT WRITE AGAIN UNLESS YOU
## 1) change the name of the file you're writing to
## 2) no longer need the data you already wrote

with open('data/gb_game_genre_data2_12_05_2014.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, fieldnames = game_and_genre_dict.keys())
    w.writeheader()

    for k in range(len(game_names)):
        w.writerow({'Name': encoding(game_names)[k],
                    'Genres': game_genres[k],
                    'Date Released': game_dates[k],
                    'Number of User Reviews': game_rv_nums[k], 
                    'Game Id': game_id_list[k]})
