### Python API Tool

I built a python script that consumes the Rails API I created for my SimplyMailStatistics.com project.

#### To get started:
Ensure you have the python dependencies installed on your machine and clone down the repo.

To run the test suite:
```
python -m unittest discover -p '*_test.py'
```

To return the delivery, opens and spam report statistics for a user:
(Use the user_id 18 to return seed data that is populated in the DB)

```
python -c 'import sumEvents; sumEvents.returnEvents(:user_id)'
```
