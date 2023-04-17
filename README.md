# Comic Information Management System

## Group 12 (Group 5 DS) Advance Programming with Python midterm project
- BI12-389 Nguyen Son 
- BI12-447 An Minh Tri
- BI12-375 Nguyen Cong Quoc
- BI12-357 Nguyen Duc Phuong
- BI12-390 Vu Hung Son

![Sample](https://github.com/Xernnn/Comics/blob/main/images/README/sample.png)


## Demo
1. Git clone this project
```
git clone https://github.com/Xernnn/Comics.git
```

2. Install the requirements
```
pip install -r requirements.txt
```

3. Install [MySQL 2.0 WorkBench](https://dev.mysql.com/downloads/file/?id=516927) 

4. Inside MySQL WorkBench, setup a new connection with these information:
- host="localhost"
- user="root"
- password="root"

5. Open [user.sql](https://github.com/Xernnn/Comics/blob/main/user.sql) script and run it

6. Import your comic data onto the database, name the database = "comics"

7. Run the python file
```
python main.py
```

## Inside the App Interface
You can find all the things you can do in this app in [this README file](https://github.com/Xernnn/Comics/tree/main/READMELATER.md)

## Example Dataset
You can find example datasets of comics inside the [example datasets](https://github.com/Xernnn/Comics/tree/main/example%20datasets) folder.

- The small dataset [comics.csv](https://github.com/Xernnn/Comics/blob/main/example%20datasets/comics(S).csv) including 10 different comics that you can easily import to test the project. 

- The larger dataset [comicsL.csv](https://github.com/Xernnn/Comics/blob/main/example%20datasets/comics(L).csv) including 135 different comics.