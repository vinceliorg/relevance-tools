import pandas as pd

def handle_uploaded_file(f):
    with open('test.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
