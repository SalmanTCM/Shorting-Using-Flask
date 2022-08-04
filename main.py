from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Index.html", **locals())


@app.route('/<int:min>/<int:max>', methods=['GET', 'POST'])
def sort(min, max):
    f = open("dataset.txt").readlines()
    d = dict()
    count = 0
    for line in f:
        line = line.replace("\n", "")
        splitted_line = line.split("\t")
        list = []
        for i in splitted_line[1:]:
            list.append(float(i))
        if( list[12] >= min and list[12] <= max):
            count = count + 1
            d[splitted_line[0]] = list
        li = []
        for i in d:
            li.append(i)
        li.sort()

    return render_template("template1.html", **locals())


if __name__ == '__main__':
    app.run()
