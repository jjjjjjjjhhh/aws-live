from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

# Configure your MariaDB database
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db = SQLAlchemy(app)

#routes

@app.route("index.html")
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

  

@app.route('/GetComOutput.html')
def GetComOutput():
   
    companies = Company.query.all()
    
    return render_template('GetComOutput.html', companies=companies)

@app.route('/GetPosOutput.html')
def GetPosOutput():
   
    positions = PositionTable.query.all()
    
    return render_template('GetPosOutput.html', positions=positions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
