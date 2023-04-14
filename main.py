from flask import Flask, request, render_template

app = Flask(__name__)

PLAYERS = [
  {
    'name': 'Aiden Markram',
    'country': 'South Africa',
    'jersey': 93,
    'bid': 10,
    'team': 'Sunrisers',
    'role': 'Batsman'
  },
  {
    'name': 'Faf Du Plessis',
    'country': 'South Africa',
    'jersey': 18,
    'bid': 10,
    'team': 'Royalchallengers',
    'role': 'Batsman'
  },
  {
    'name': 'Rohit Sharma',
    'country': 'India',
    'jersey': 45,
    'bid': 10,
    'team': 'MumIndians',
    'role': 'Batsman'
  },
  {
    'name': 'MS Dhoni',
    'country': 'India',
    'jersey': 7,
    'bid': 10,
    'team': 'Superkings',
    'role': 'Keeper'
  },
  {
    'name': 'KL Rahul',
    'country': 'India',
    'jersey': 1,
    'bid': 10,
    'team': 'Supergiants',
    'role': 'Batsman'
  },
  {
    'name': 'Nitish Rana',
    'country': 'India',
    'jersey': 27,
    'bid': 10,
    'team': 'Knightriders',
    'role': 'Batsman'
  },
  {
    'name': 'Sanju Samson',
    'country': 'India',
    'jersey': 9,
    'bid': 10,
    'team': 'Royals',
    'role': 'Keeper'
  },
  {
    'name': 'Shikhar Dhawan',
    'country': 'India',
    'jersey': 25,
    'bid': 10,
    'team': 'PbKings',
    'role': 'Batsman'
  },
  {
    'name': 'David Warner',
    'country': 'Australia',
    'jersey': 31,
    'bid': 10,
    'team': 'Capitals',
    'role': 'Batsman'
  },
  {
    'name': 'Hardik Pandya',
    'country': 'India',
    'jersey': 33,
    'bid': 10,
    'team': 'Titans',
    'role': 'Bowler'
  },
]


@app.route("/")
def hello_world():
  return render_template('iplauction.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)