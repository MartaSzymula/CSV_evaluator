# CSV_evaluator

This tool was created to evaluate synonym pairs with a True/False answer and comment if needed.

## Requirements

This project requires Python 3.9 and requirements described in file `requirements.txt`

```bash
pip install -r requirements.text
```

## Run server

```bash
python manage.py runserver
```

## Input data

Input data is `base_file.csv` file placed in `CSV_evaluator\validation_app\static`.
First & second columns are synonyms, followed by answer & comment column.
Sample file is provided in the repository.

## Output data

Output file can be downloaded as .csv file.
