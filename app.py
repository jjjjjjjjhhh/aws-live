from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, String, Date, Integer
import config

app = Flask(__name__)

# Configure your MariaDB database
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db = SQLAlchemy(app)

#routes

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

@app.route("/job-details-1.html")
def jobdetail1():
    return render_template('job-detail-1.html')

@app.route("/job-details-2.html")
def jobdetail2():
    return render_template('job-detail-2.html')

@app.route("/job-details-3.html")
def jobdetail3():
    return render_template('job-detail-3.html')

@app.route("/job-details-4.html")
def jobdetail4():
    return render_template('job-detail-4.html')

@app.route("/job-details-5.html")
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

    student_id = Column(String(5), primary_key=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(12), nullable=False)
    email = Column(String(50), nullable=False)
    company = Column(String(50), nullable=False)
    position = Column(String(50), nullable=False)
    start_date = Column(String(50), nullable=False)
    end_date = Column(String(50), nullable=False)


class Lecturer(db.Model):
    __tablename__ = 'Lecturer'
    __table_args__ = {'schema': 'employee'} 

    lecturer_id = Column(String(4), primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(12), nullable=False)
    specialisation = Column(String(50), nullable=False)
  
class Report(db.Model):
    __tablename__ = 'Report'
    __table_args__ = {'schema': 'employee'} 

    report_id = Column(String(5), primary_key=True)
    student_id = Column(String(5), nullable=False)
    submission_date = Column(Date, nullable=False)

class Evaluation(db.Model):
    __tablename__ = 'Evaluation'
    __table_args__ = {'schema': 'employee'} 

    evaluation_id = Column(String(5), primary_key=True)
    lecturer_id = Column(String(4), nullable=False)
    report_id = Column(String(5),  nullable=False)
    score = Column(Integer, nullable=False)
    feedback = Column(String(255), nullable=False)



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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
