# homework_12

## Installation

1. Clone the repository

* `git clone https://github.com/yo1am1/homework_12.git`

2. Go to the directory

* `cd homework_12`

3. Install dependencies

* `pip install -r requirements.txt`

4. Run docker

* `docker run -p 6379:6379 redis`

5. Run the application (and create the db if it doesn't exist)

* `py manage.py makemigrations`
* `py manage.py migrate`
* `py manage.py runserver`

5. Generate the publications with custom command:

* `py manage.py generate_publication --count {int: AMOUNT}`
> There is a parametr --count {int: AMOUNT}, where {AMOUNT} is a number of publications you will generate (dafault = 1)

7. Go to the site

* [Home page](https://localhost:8000/)

> Input "http://localhost:8000/publication/{YOUR_ID}" in your browser to see the publication with the id = {YOUR_ID}
