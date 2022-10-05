# CTFd-Add-User
A small python application made to add users from a CSV 

This application is originally made for education providers to add lists of students to their CTFd instance. 

# Installation

Install requirements:
```py
pip install -r requirements.txt
```

# Configuration

Fill in relevant information in `config.py`:

`APIKEY` can be found in `<CTF link>/settings#tokens`

`BASEURL` is the base URL used for the CTF

# CSV
The CSV should be as shown in [users.csv](https://github.com/BritishBenji/CTFd-Add-User/blob/main/users.csv)

It consists of `Username`,`Email`,`Password`


# Running the program
Run the program with `python3 app.py`
