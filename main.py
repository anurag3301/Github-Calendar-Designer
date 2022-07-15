import grid_ui
import commiter
import random

YEAR = 2019
REPO_DIR = '/home/anurag/repo/test'
USERFULLNAME = 'Anurag Kumar Singh'
USEREMAIL = 'anurag3301.0x0@gmail.com'
UPPER_LIMIT = 5
LOWER_LIMIT = 2

if __name__ == "__main__":
    dates = grid_ui.get_dates(YEAR)
    for i in dates:
        for j in range(random.randint(LOWER_LIMIT, UPPER_LIMIT)):
            commiter.commit(i)
