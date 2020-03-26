"""standard freeze script"""

from flask_frozen import Freezer

# instead of "filename," below, use the name of the file that
# runs YOUR Flask app - omit .py from the filename
from filename import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
