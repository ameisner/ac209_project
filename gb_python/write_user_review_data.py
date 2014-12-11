# written by Mobolaji Williams,
# AC209-Final Proj

# This code writes the user review data to a stable file. 
# Date and time of writing: 12/4/2014 7:32 PM

## DO NOT WRITE AGAIN UNLESS YOU
## 1) change the name of the file you're writing to
## 2) no longer need the data you already wrote

with open('data/gb_user_review_data_12_04_2014.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, fieldnames = usr_rv_dict.keys())
    w.writeheader()

    for k in range(len(usr_g_names)):
        w.writerow({'Name': encoding(usr_g_names)[k], 'User Review Score': usr_g_score[k], 'User Reviewer': usr_g_reviewer[k], 'Date of Review':usr_g_rv_date[k], 
               'Game Id': g_id[k] })
