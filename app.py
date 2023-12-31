from curses import flash
from flask import Flask, render_template, request, redirect, url_for
from flask_s3 import FlaskS3
from flask_sqlalchemy import SQLAlchemy
import os
import boto3
from botocore.exceptions import NoCredentialsError
#from sqlalchemy import Column, String, String, Date, Integer

from config import *


bucket = custombucket
region = customregion

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['FLASKS3_BUCKET_NAME'] = custombucket
app.config['FLASKS3_REGION'] = customregion
db = SQLAlchemy(app)

s3 = FlaskS3(app)

#routes

@app.route("/")
def root():
    return render_template("/index.html")


@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/admin.html")
def admin():
    return render_template('admin.html')

@app.route("/adminCom.html")
def adminCom():
    return render_template('adminCom.html')

@app.route("/adminLec.html")
def adminLec():
    return render_template('adminLec.html')

@app.route("/adminStud.html")
def adminStud():
    return render_template('adminStud.html')

@app.route("/AfterSubmit.html")
def AfterSubmit():
    return render_template('AfterSubmit.html')

@app.route("/job-detail-1.html")
def jobdetail1():
    return render_template('job-detail-1.html')

@app.route("/job-detail-2.html")
def jobdetail2():
    return render_template('job-detail-2.html')

@app.route("/job-detail-3.html")
def jobdetail3():
    return render_template('job-detail-3.html')

@app.route("/job-detail-4.html")
def jobdetail4():
    return render_template('job-detail-4.html')

@app.route("/job-detail-5.html")
def jobdetail5():
    return render_template('job-detail-5.html')

@app.route("/portfolio.html")
def portfolio():
    return render_template('portfolio.html')


# Define model
class Company(db.Model):
    __tablename__ = 'Company'  # Table name (case-sensitive)
    __table_args__ = {'schema': 'employee'}  # Schema name
    
    
    company_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    state = db.Column(db.String(255))
    pic_name = db.Column(db.String(255))
    pic_email = db.Column(db.String(255))
    pic_phone_number = db.Column(db.String(255))

class PositionTable(db.Model):
    __tablename__ = 'PositionTable'  # Table name (case-sensitive)
    __table_args__ = {'schema': 'employee'}  # Schema name
    
    
    position_id = db.Column(db.String(5), primary_key=True)
    company_id = db.Column(db.String(5), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    job_desc = db.Column(db.String(255), nullable=False)
    allowance = db.Column(db.DECIMAL(precision=6, scale=2), nullable=False)

class StudentApplication(db.Model):
    __tablename__ = 'StudentApplication'
    __table_args__ = {'schema': 'employee'} 

    application_id = db.Column(db.String(5), primary_key=True)
    company_id = db.Column(db.String(5), nullable=False)
    position_id = db.Column(db.String(5),  nullable=False)
    student_id = db.Column(db.String(5), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    major = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.DATE, nullable=False)
    end_date = db.Column(db.DATE, nullable=False)

class Student(db.Model):
    __tablename__ = 'Student'
    __table_args__ = {'schema': 'employee'} 

    student_id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    company = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50), nullable=False)


class Lecturer(db.Model):
    __tablename__ = 'Lecturer'
    __table_args__ = {'schema': 'employee'} 

    lecturer_id = db.Column(db.String(4), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    specialisation = db.Column(db.String(50), nullable=False)
  
class Report(db.Model):
    __tablename__ = 'Report'
    __table_args__ = {'schema': 'employee'} 

    report_id = db.Column(db.String(5), primary_key=True)
    student_id = db.Column(db.String(5), nullable=False)
    submission_date = db.Column(db.Date, nullable=False)

class Evaluation(db.Model):
    __tablename__ = 'Evaluation'
    __table_args__ = {'schema': 'employee'} 

    evaluation_id = db.Column(db.String(5), primary_key=True)
    lecturer_id = db.Column(db.String(4), nullable=False)
    report_id = db.Column(db.String(5),  nullable=False)
    score = db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.String(255), nullable=False)


#retrive data
@app.route('/GetComOutput.html')
def GetComOutput():
   
    companies = Company.query.all()
    
    return render_template('GetComOutput.html', companies=companies)

@app.route('/GetStuAppliOutput.html')
def GetStuAppliOutput():
   
    studentsAppli = StudentApplication.query.all()
    
    return render_template('GetStuAppliOutput.html', studentsAppli=studentsAppli)

@app.route('/GetPosOutput.html')
def GetPosOutput():
   
    positions = PositionTable.query.all()
    
    return render_template('GetPosOutput.html', positions=positions)

@app.route('/GetLecOutput.html')
def GetLecOutput():
   
    lecturers = Lecturer.query.all()
    
    return render_template('GetLecOutput.html', lecturers=lecturers)

@app.route('/GetReportOutput.html')
def GetReportOutput():
   
    reports = Report.query.all()
    
    return render_template('GetReportOutput.html', reports=reports)

@app.route('/GetScoreOutput.html')
def GetScoreOutput():
   
    scores = Evaluation.query.all()
    
    return render_template('GetScoreOutput.html', scores=scores)

@app.route('/GetStudOutput.html')
def GetStudOutput():
   
    students = Student.query.all()
    
    return render_template('GetStudOutput.html', students=students)


#store data

@app.route("/AddCom.html")
def add_com_form():
    return render_template("AddCom.html")

@app.route("/add_com", methods=["POST"])
def add_com():
    if request.method == "POST":
        company_id = request.form["companyId"]
        name = request.form["companyName"]
        industry = request.form["companyIndustry"]
        state = request.form["companyState"]
        pic_name = request.form["contactName"]
        pic_email = request.form["contactEmail"]
        pic_phone_number = request.form["phoneNumber"]
        
        new_company = Company(company_id=company_id, name=name, industry=industry, state=state, pic_name=pic_name, pic_email=pic_email, pic_phone_number=pic_phone_number)
        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for("add_pos_form"))

@app.route("/AddPos.html")
def add_pos_form():
    return render_template("AddPos.html")

@app.route("/add_pos", methods=["POST"])
def add_pos():
    if request.method == "POST":
        position_id = request.form["posId"]
        company_id = request.form["posComId"]
        position = request.form["posName"]
        job_desc = request.form["jobDesc"]
        allowance = request.form["jobPay"]
        
        new_position = PositionTable(position_id=position_id, company_id=company_id, position=position, job_desc=job_desc, allowance=allowance)
        db.session.add(new_position)
        db.session.commit()

        return redirect(url_for("after_submit"))

@app.route("/AddScore.html")
def add_score_form():
    return render_template("AddScore.html")

@app.route("/add_score", methods=["POST"])
def add_score():
    if request.method == "POST":
        evaluation_id = request.form["inScoreEvaId"]
        lecturer_id = request.form["inScoreLecId"]
        report_id = request.form["inScoreReportId"]
        score = request.form["inScoreScore"]
        feedback = request.form["inScoreFeed"]
        
        new_score = Evaluation(evaluation_id=evaluation_id, lecturer_id=lecturer_id, report_id=report_id, score=score, feedback=feedback)
        db.session.add(new_score)
        db.session.commit()

        return redirect(url_for("after_submit"))


@app.route("/AddReport.html")
def add_report_form():
    return render_template("AddReport.html")

@app.route("/add_report", methods=["POST"])
def add_report():
    if request.method == "POST":
        report_id = request.form["reportId"]
        student_id = request.form["reportStudId"]
        submission_date = request.form["reportDate"]
        report_file = request.files["reportPDF"]

        # cursor = db.session.cursor()
        if report_file.filename == "":
            return "Please select a file"

        try:
            new_report = Report(report_id=report_id, student_id=student_id, submission_date=submission_date)
            db.session.add(new_report)
            db.session.commit()

            # Upload the report file to S3
            report_name_in_s3 = f"{student_id}_Report"
            s3 = boto3.resource('s3')

            print("Data inserted in MySQL RDS... uploading report to S3...")
            s3.Bucket(custombucket).put_object(Key=report_name_in_s3, Body=report_file)
            bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
            s3_location = (bucket_location['LocationConstraint'])

            if s3_location is None:
                s3_location = ''
            else:
                s3_location = '-' + s3_location

            object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
                s3_location,
                custombucket,
                report_name_in_s3)

           
            return redirect(url_for("after_submit"))

        except Exception as e:
            return str(e)

    
    return "Report submission failed."

     
        
@app.route("/AddStudApply.html")
def add_apply_form():
    return render_template("AddStudApply.html")

@app.route("/add_apply", methods=["POST"])
def add_apply():
    if request.method == "POST":
        application_id = request.form["inStudApplyID"]
        company_id = request.form["inStudComID"]
        position_id = request.form["inStudPosID"]
        student_id = request.form["inStudStuID"]
        name = request.form["inStudName"]
        phone_number = request.form["inStudPhoneNumber"]
        email = request.form["inStudEmail"]
        major = request.form["inStudMajor"]
        start_date = request.form["inStudStartDate"]
        end_date = request.form["inStudEndDate"]
        resume_file = request.files["inStudResume"]
        
        if resume_file.filename == "":
            return "Please select a file"

        try:
            new_apply = StudentApplication(application_id=application_id, company_id=company_id, position_id=position_id, 
            student_id=student_id, name=name, phone_number=phone_number, email=email, major=major, start_date=start_date, end_date=end_date)
            db.session.add(new_apply)
            db.session.commit()

            
            resume_name_in_s3 = f"{student_id}_Resume"
            s3 = boto3.resource('s3')

            print("Data inserted in MySQL RDS... uploading report to S3...")
            s3.Bucket(custombucket).put_object(Key=resume_name_in_s3, Body=resume_file)
            bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
            s3_location = (bucket_location['LocationConstraint'])

            if s3_location is None:
                s3_location = ''
            else:
                s3_location = '-' + s3_location

            object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
                s3_location,
                custombucket,
                resume_name_in_s3)

            
            return redirect(url_for("after_submit"))

        except Exception as e:
            return str(e)

    
    return "Application submission failed."
        
#update and delete

@app.route("/modifyOrDelete.html" , methods=["GET", "POST"])
def search_student():

   
    if request.method == "POST":

        
        student_id = request.form["searchStudId"]
        print("Student ID entered:", student_id)
        student = Student.query.get(student_id)

        return redirect(url_for("display_student", student_id=student.student_id))
        


    return render_template("modifyOrDelete.html")

@app.route("/displayStudent.html", methods=["GET", "POST"])
def display_student():
    
    student_id = request.args.get("student_id")
    print("Student ID entered:", student_id)
    student = Student.query.get(student_id)
    if not student:
        flash("Student not found. Please enter a valid student ID.")
        return redirect(url_for("search_student")) 

    if request.form.get("searchModify"):
        return redirect(url_for("modify_student", student_id=student.student_id))

        
    if request.form.get("searchDelete"):
        return redirect(url_for("confirm_delete", student_id=student.student_id))


    return render_template("displayStudent.html", student=student)






@app.route("/ModifyStudent.html/<string:student_id>", methods=["GET", "POST"])
def modify_student(student_id):
    student = Student.query.get(student_id)
    if request.method == "POST":
        
        student.name = request.form.get("modifyStudName", student.name)
        student.phone_number = request.form.get("modifyStudPhone", student.phone_number)
        student.email = request.form.get("modifyStudEmail", student.email)
        student.company = request.form.get("modifyStudCom", student.company)
        student.position = request.form.get("modifyStudPos", student.position)
        student.start_date = request.form.get("modifyStudSDate", student.start_date)
        student.end_date = request.form.get("modifyStudEDate", student.end_date)
        db.session.commit()
        #flash("Student information updated successfully.")
        return redirect(url_for("after_submit"))

    return render_template("ModifyStudent.html", student=student)



@app.route("/confirmDeleteStud.html/<string:student_id>", methods=["GET", "POST"])
def confirm_delete(student_id):
    student = Student.query.get(student_id)
    #studentReport = Report.query.get(student_id)
    if request.method == "POST":
       # db.session.delete(studentReport)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for("after_submit"))

    return render_template("confirmDeleteStud.html", student=student)


@app.route("/modifyOrDeleteL.html" , methods=["GET", "POST"])
def search_lecturer():

   
    if request.method == "POST":

        
        lecturer_id = request.form["searchLecId"]
        print("Lecturer ID entered:", lecturer_id)
        lecturer = Lecturer.query.get(lecturer_id)

        return redirect(url_for("display_lecturer", lecturer_id=lecturer.lecturer_id))
        


    return render_template("modifyOrDeleteL.html")

@app.route("/displayLecturer.html", methods=["GET", "POST"])
def display_lecturer():
    
    lecturer_id = request.args.get("lecturer_id")
    print("lecturer ID entered:", lecturer_id)
    lecturer = Lecturer.query.get(lecturer_id)
    if not lecturer:
        flash("Lecturer not found. Please enter a valid lecturer ID.")
        return redirect(url_for("search_lecturer")) 

    if request.form.get("searchModifyL"):
        return redirect(url_for("modify_lecturer", lecturer_id=lecturer.lecturer_id))

        
    if request.form.get("searchDeleteL"):
        return redirect(url_for("confirm_delete_lecturer", lecturer_id=lecturer.lecturer_id))


    return render_template("displayLecturer.html", lecturer=lecturer)






@app.route("/ModifyLecturer.html/<string:lecturer_id>", methods=["GET", "POST"])
def modify_lecturer(lecturer_id):
    lecturer = Lecturer.query.get(lecturer_id)
    if request.method == "POST":
        
        lecturer.name = request.form.get("modifyLecName", lecturer.name)
        lecturer.email = request.form.get("modifyLecEmail", lecturer.email)
        lecturer.phone_number = request.form.get("modifyLecPhone", lecturer.phone_number)
        lecturer.specialisation = request.form.get("modifyLecDate", lecturer.specialisation)
        db.session.commit()
        
        return redirect(url_for("after_submit"))

    return render_template("ModifyLecturer.html",lecturer=lecturer)



   

@app.route("/confirmDeleteLec.html/<string:lecturer_id>", methods=["GET", "POST"])
def confirm_delete_lecturer(lecturer_id):
    lecturer = Lecturer.query.get(lecturer_id)
    
    if request.method == "POST":
       
        db.session.delete(lecturer)
        db.session.commit()
        return redirect(url_for("after_submit"))

    return render_template("confirmDeleteLec.html", lecturer=lecturer)


@app.route("/modifyOrDeleteC.html" , methods=["GET", "POST"])
def search_company():

   
    if request.method == "POST":

        
        company_id = request.form["searchComId"]
        print("Company ID entered:", company_id)
        company = Company.query.get(company_id)

        return redirect(url_for("display_company", company_id=company.company_id))
        


    return render_template("modifyOrDeleteC.html")

@app.route("/modifyOrDeleteP.html" , methods=["GET", "POST"])
def search_position():

   
    if request.method == "POST":

        
        position_id = request.form["searchPosId"]
        print("position ID entered:", position_id)
        position = PositionTable.query.get(position_id)

        return redirect(url_for("display_position", position_id=position.position_id))
        


    return render_template("modifyOrDeleteP.html")

@app.route("/displayCompany.html", methods=["GET", "POST"])
def display_company():
    
    company_id = request.args.get("company_id")
    print("company ID entered:", company_id)
    company = Company.query.get(company_id)
    if not company:
        flash("company not found. Please enter a valid company ID.")
        return redirect(url_for("search_company")) 

    if request.form.get("searchModifyC"):
        return redirect(url_for("modify_company", company_id=company.company_id))

        
    if request.form.get("searchDeleteC"):
        return redirect(url_for("confirm_delete_company", company_id=company.company_id))


    return render_template("displayCompany.html", company=company)


@app.route("/displayPosition.html", methods=["GET", "POST"])
def display_position():
    
    position_id = request.args.get("position_id")
    print("position ID entered:", position_id)
    position = PositionTable.query.get(position_id)
    if not position:
        flash("position not found. Please enter a valid position ID.")
        return redirect(url_for("search_position")) 

    if request.form.get("searchModifyP"):
        return redirect(url_for("modify_position", position_id=position.position_id))

        
    if request.form.get("searchDeleteP"):
        return redirect(url_for("confirm_delete_position", position_id=position.position_id))


    return render_template("displayPosition.html", position=position)



@app.route("/ModifyCompany.html/<string:company_id>", methods=["GET", "POST"])
def modify_company(company_id):
    company = Company.query.get(company_id)
    if request.method == "POST":
        
        company.name = request.form.get("modifyComName", company.name)
        company.industry = request.form.get("modifyComIndus", company.industry)
        company.state = request.form.get("modifyComState", company.state)
        company.pic_name = request.form.get("modifyComPicName", company.pic_name)
        company.pic_email = request.form.get("modifyComEmail", company.pic_email)
        company.pic_phone_number = request.form.get("modifyComPhone", company.pic_phone_number)
        
        db.session.commit()
        
        return redirect(url_for("after_submit"))

    return render_template("ModifyCompany.html",company=company)

@app.route("/ModifyPosition.html/<string:position_id>", methods=["GET", "POST"])
def modify_position(position_id):
    position = PositionTable.query.get(position_id)
    if request.method == "POST":
        
        position.position = request.form.get("modifyPosName", position.position)
        position.job_desc = request.form.get("modifyPosJob", position.job_desc)
        position.allowance = request.form.get("modifyPosPay", position.allowance)
        
        
        db.session.commit()
        
        return redirect(url_for("after_submit"))

    return render_template("ModifyPosition.html",position=position)

   

@app.route("/confirmDeleteCom.html/<string:company_id>", methods=["GET", "POST"])
def confirm_delete_company(company_id):
    company = Company.query.get(company_id)
    
    if request.method == "POST":
       
        db.session.delete(company)
        db.session.commit()
        return redirect(url_for("after_submit"))

    return render_template("confirmDeleteCom.html", company=company)

@app.route("/confirmDeletePos.html/<string:position_id>", methods=["GET", "POST"])
def confirm_delete_position(position_id):
    position = PositionTable.query.get(position_id)
    
    if request.method == "POST":
       
        db.session.delete(position)
        db.session.commit()
        return redirect(url_for("after_submit"))

    return render_template("confirmDeletePos.html", position=position)        

        

@app.route("/AfterSubmit.html")
def after_submit():
    return render_template("AfterSubmit.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
