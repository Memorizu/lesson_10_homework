from flask import Flask

from utils import get_all, get_by_pk, get_by_skill


app = Flask(__name__)


@app.route('/')
def page_index():
    """
    Главная страничка со всеми кандидатами
    :return:Все кандидаты
    """
    candidates = get_all()
    result = "<br>"
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += "<br>"
    return f"<pre> {result} </pre>"


@app.route('/candidate/<int:pk>')
def get_candidate(pk):
    """
    Поиск кандидата по PK
    :param pk: int
    :return: Кандидат с искомым PK
    """
    candidate = get_by_pk(pk)
    url = candidate['picture']
    result = "<br>"
    result += candidate['name'] + "<br>"
    result += candidate['position'] + "<br>"
    result += candidate['skills'] + "<br>"
    return f'<pre> <img src = "{url}"> <br> {result} <pre>'


@app.route('/candidate/skill/<skill>')
def get_candidate_on_skills(skill):
    """
    Поиск кандидата по навыкам
    :param skill: Искомый навык
    :return: Кандидата, обладающий нужным навыком
    """
    candidates = get_by_skill(skill)
    result = "<br>"
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += "<br>"
    return f'<pre> {result} <pre>'


if __name__ == '__main__':
    app.run(debug=True)


