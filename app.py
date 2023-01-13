from flask import Flask, render_template, request
from jira import JIRA
import datetime

app = Flask(__name__)

# Connect to JIRA
jira = JIRA(basic_auth=('username', 'password'), server='https://yourjira.com')

@app.route('/', methods=['GET', 'POST'])
def get_defects():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
    else:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')

    # Get all issues from JIRA with 'defect' label and created within the specified time frame
    defects = jira.search_issues('labels = defect and created >= {} and created <= {}'.format(start_date, end_date))

    # Extract defect summary and key from each issue
    defects_list = []
    for defect in defects:
        defects_list.append({'summary': defect.fields.summary, 'key': defect.key})

    return render_
