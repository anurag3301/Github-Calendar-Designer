# Github-Calendar-Designer
Create Creative Designs using Github Calendar
![Untitled](https://user-images.githubusercontent.com/52702259/179017623-de7e8342-054f-4015-85ee-8d31ae60d414.png)

![Untitled](https://user-images.githubusercontent.com/52702259/179019294-e6ce5223-fb85-41a8-bd41-9fbfd264b3d9.png)

### Install the deps
```sh
pip install pygame python-dateutil
```

### Open `main.py` file and edit these configurations
```py
YEAR = 2020     # The year you wanna operate on
REPO_DIR = '/home/anurag/repo/test'     # Path of the repository where all the commits will happen
USERNAME = '0xpar'  # Your Full Name on Github for specifing the autor in commits
USEREMAIL = 'anurag3301.0x0@gmail.com'      # Your Email on Github for specifing the author in commit 
UPPER_LIMIT = 5     # Max no of commit per day 
LOWER_LIMIT = 2     # Min no of commit per day
# The no of commit on a day is determined randomly between the upper and lower limit
# Set both UPPER_LIMIT and LOWER_LIMIT to same no to have a constent commit no.
```

### Follow the steps
1. After updating the main.py, run it
2. A window will apper, design whatever you want on the grid, then click on `start` to start the commit process
3. There is a option to save your design, draw whatever you want and then click on `save and exit` it will create a new <year>.pkl file will stores the design data. It can be retrived by running the program again and click on `old` button. It will retrive the stored design.
4. The designs are stored with the corresponding year
5. If you have git commit signing turned on, the program will turn it off for that particular repo cuz signing commits takes a hell lot of time.
6. The program only commits, you'll have to push it yourself.

## Hope you find it fun and if make some creative designs please send it me, ill link it or keep it as display, catch you some other fun project :)
