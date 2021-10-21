from flask import Flask, render_template, request
from accountant import manager

app = Flask(__name__)
manager.read_file()


@app.route("/", methods=["GET", "POST"])
def main():
    mode = request.form.get('mode')
    params = []
    if mode == 'saldo':
        params.append(int(request.form.get('amount')))
    elif mode == 'zakup':
        params.append(request.form.get('name'))
        params.append(int(request.form.get('count')))
        params.append(int(request.form.get('amount')))
    elif mode == 'sprzedaz':
        params.append(request.form.get('name'))
        params.append(int(request.form.get('count')))
        params.append(int(request.form.get('amount')))
    manager.execute(mode, params)
    manager.logs_write_file()
    manager.write_file()
    return render_template("index.html", saldo=manager.saldo, store=manager.store)


manager.logs_read_file()


@app.route("/history/<index_start>/<index_stop>", methods=["GET", "POST"])
@app.route("/history")
def history(index_start=None, index_stop=None):

    if not index_start:
        index_start = 0
    if not index_stop:
        index_stop = len(manager.logs)
    history = manager.logs[int(index_start): int(index_stop)]

    context = {
        "name": "Adam",
        "start": index_start,
        "stop": index_stop
    }
    return render_template("history.html", history=history, context=context)


if __name__ == '__main__':
    app.run()
