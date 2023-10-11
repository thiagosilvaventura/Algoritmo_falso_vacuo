from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Tamanho da tabela
rows = 5
cols = 5
table = [[(i * cols + j + 1) for j in range(cols)] for i in range(rows)]
merged = [[False for _ in range(cols)] for _ in range(rows)]

@app.route('/')
def index():
    return render_template('index.html', table=table, rows=rows, cols=cols)

@app.route('/merge', methods=['POST'])
def merge():
    delta = int(request.form['delta'])
    merge_cells(delta)
    return render_template('index.html', table=table, rows=rows, cols=cols)

def merge_cells(delta):
    for i in range(0, rows, delta):
        for j in range(0, cols, delta):
            merge_group(i, j, delta)

def merge_group(row, col, delta):
    average = 0
    count = 0

    for i in range(row, row + delta):
        for j in range(col, col + delta):
            average += table[i][j]
            count += 1

    average //= count

    for i in range(row, row + delta):
        for j in range(col, col + delta):
            table[i][j] = average
            merged[i][j] = True

@app.route('/reset')
def reset():
    for i in range(rows):
        for j in range(cols):
            table[i][j] = (i * cols + j + 1)
            merged[i][j] = False
    return render_template('index.html', table=table, rows=rows, cols=cols)

if __name__ == '__main__':
    app.run(debug=True)
