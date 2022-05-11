from flask import Blueprint, abort, render_template

bp = Blueprint('pages', __name__)
VISUALIZERS = ('papaya', 'xtk')


@bp.route('/<name>')
def visualizer(name):
    if name in VISUALIZERS:
        return render_template(f'{name}.html')
    abort(404)
