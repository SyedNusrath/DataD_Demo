"""
    app.py
    ~~~~~~
    This simple sample application provides a bare-bones website that allows
    you to:
    - Create new user accounts.
    - Log into existing user accounts.
    - View a simple dashboard page that displays user information.
    - Edit your user information on said dashboard page.
    - Log out of the website.
    Please see the README for more information of how to run and use this
    sample application.
"""


from os import environ

from flask import Flask, redirect, render_template, request, url_for
import mysql_connection as sql_c
import ast

app = Flask(__name__)

##### Website
@app.route('/')
def index():
    """Basic home page."""
    return render_template('index.html')
	

@app.route('/form')
def form():
    """Basic home page."""
    return render_template('form.html')


@app.route('/login')
def login():
    """Basic home page."""
    return render_template('login.html')

@app.route('/register')
def register():
    """Basic home page."""
    return render_template('register.html')

@app.route('/view_questionnaire_details', methods=['POST'])
def view_questionnaire_details():
    """Basic home page."""
    print("in view_questionnaire_details",request.json['customer_id'])
    rows = sql_c.select_where_query("others_customer_questions","customer_name",str(request.json['customer_id']))
    print(rows)
    return str(rows)

@app.route('/forgot_password')
def forgot_password():
    """Basic home page."""
    return render_template('forgot-password.html')

@app.route('/project_school_details')
def project_school_details():
    """Basic home page."""
    rows = sql_c.selectquery('customer_details')
    print(rows)
    return render_template('customer_details.html',rows = rows)

@app.route('/form_details', methods=['POST'])
def form_details():
    """Basic home page."""
    # print('inside form details',request.form.get('school_name'))
    # print('inside form details',request.form['your_web_site_allows_plugin'])
    school_name= request.form['school_name']
    official_email_address= request.form['official_email_address']
    contact_number= request.form['contact_number']
    admission_info= request.form['admission_info']
    school_syllabus= request.form['school_syllabus']
    Classes_you_offer= request.form['Classes_you_offer']
    school_timing= request.form['school_timing']
    school_fee_info= request.form['school_fee_info']
    transportation_details= request.form['transportation_details']
    alternate_number= request.form['alternate_number']
    school_working_hours= request.form['school_working_hours']
    school_calendar= request.form['school_calendar']
    your_web_site_url= request.form['your_web_site_url']
    your_web_site_cloud_onprimise= request.form['your_web_site_cloud_onprimise']
    your_web_site_allows_plugin= request.form['your_web_site_allows_plugin']

    values = (school_name, official_email_address, contact_number, admission_info, school_syllabus, Classes_you_offer, school_timing, school_fee_info, transportation_details, alternate_number, school_working_hours, school_calendar, your_web_site_url, your_web_site_cloud_onprimise, your_web_site_allows_plugin)
    columns = ("school_name" , "official_email_address" , "contact_number" , "admission_info" , "school_syllabus" , "Classes_you_offer" , "school_timing" , "school_fee_info" , "transportation_details" , "alternate_number" , "school_working_hours" , "school_calendar" , "your_web_site_url" , "your_web_site_cloud_onprimise" , "your_web_site_allows_plugin")
    sql_c.insertQuery('datad_demo.customer_details',str(columns).replace("'","").replace('"',""),str(values))

    return render_template('form.html')

@app.route('/other_question_anwsers', methods=['POST'])
def other_question_anwsers():
    """Basic home page."""
    print("in other_question_anwsers")
    customer_id_arr=ast.literal_eval(request.json['customer_id_arr'])
    question_arr=ast.literal_eval(request.json['question_arr'])
    awnser_arr=ast.literal_eval(request.json['awnser_arr'])
    print(type(customer_id_arr),question_arr,awnser_arr)
    for cus,qes,awn in zip(customer_id_arr,question_arr,awnser_arr):
        columns = ("customer_name","question","answer")
        print(columns,(cus,qes,awn))
        sql_c.insertQuery("datad_demo.others_customer_questions",str(columns).replace("'","").replace('"',""),str((cus,qes,awn)))
    return str("successfully added to database")

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5002, use_reloader=True)