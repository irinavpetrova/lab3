import datetime
import matplotlib.pyplot as plt


def count_bdate(bdate_list):
    age = []
    curr_date = datetime.date.today()
    for i in bdate_list:
        t_date = i.split(sep='.')

        if int(curr_date.month) > int(t_date[1]):
            age.append(int(curr_date.year) - int(t_date[2]))

        elif int(curr_date.month) == int(t_date[1]):
            if int(curr_date.day) > int(t_date[2]):
                age.append(int(curr_date.year) - int(t_date[2]))

            else:
                age.append(int(curr_date.year) - int(t_date[2]) - 1)

        elif int(curr_date.month) < int(t_date[1]):
            age.append(int(curr_date.year) - int(t_date[2]) - 1)

    return age


def gist(ages_list):
    plt.hist(ages_list)
    plt.show()  # -*- coding: utf-8 -*-

