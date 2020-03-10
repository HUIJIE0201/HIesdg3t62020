from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# with docker
# from os import environ

app = Flask(__name__)

# with docker
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')

# without docker
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/clinic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)
 
class Clinic(db.Model):
    __tablename__ = 'clinic'
 
    clinicName = db.Column(db.String(100), primary_key=True)
    doctorName = db.Column(db.String(100), primary_key=True)
    groupedLocation = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    postalCode = db.Column(db.Integer, nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    contactNumber = db.Column(db.String(15), nullable=False)
 
    def __init__(clinicName, doctorName, groupedLocation, address, postalCode, specialty, contactNumber):
        self.clinicName = clinicName
        self.doctorName = doctorName
        self.groupedLocation = groupedLocation
        self.address = address
        self.postalCode = postalCode
        self.specialty = specialty
        self.contactNumber = contactNumber
 
    def json(self):
        return {"clinicName": self.clinicName, "doctorName": self.doctorName, "groupedLocation": self.groupedLocation, "address": self.address, "postalCode": self.postalCode, "specialty": self.specialty, "contactNumber": self.contactNumber}
class ClinicOpening(db.Model):
    __tablename__ = 'clinicOpening'
 
    clinicName = db.Column(db.String(100), primary_key=True)
    openingDays = db.Column(db.String(20), primary_key=True)
    openingHour = db.Column(db.String(10), primary_key=True)
    closingHour = db.Column(db.String(10), nullable=False)
 
    def __init__(clinicName, openingDays, openingHour, closingHour):
        self.clinicName = clinicName
        self.openingDays = openingDays
        self.openingHour = openingHour
        self.closingHour = closingHour
 
    def json(self):
        return {"clinicName": self.clinicName, "openingDays": self.openingDays, "openingHour": self.openingHour, "closingHour": self.closingHour}

# get all clinics
@app.route("/clinic")
def get_all():
    # query for clinic alone
	# return jsonify({"clinic": [clinic.json() for clinic in Clinic.query.all()]})

    # query for clinic and opening hours
    return jsonify({"clinic": [clinic.json() for clinic in Clinic.query(Clinic).join(ClinicOpening).all()]})

#get clinics from name with %
@app.route("/clinic/<string:clinicName>")
def find_by_clinicName(clinicName):
    clinic = Clinic.query(Clinic).join(ClinicOpening).filter(clinicName.like(f'%{clinicName}%')).all()
    if clinic:
        return jsonify(clinic.json())
    return jsonify({"message": "Clinic not found."}), 404

# get clinics by location group
@app.route("/clinic/<string:groupedLocation>")
def find_by_groupedLocation(groupedLocation):
    groupedLocation = Clinic.query(Clinic).join(ClinicOpening).filter_by(groupedLocation=groupedLocation).all()
    if groupedLocation:
        return jsonify(groupedLocation.json())
    return jsonify({"message": "No clinics found."}), 404

# Create clinic
# @app.route("/clinic/<string:clinicName>", methods=['POST'])
# def create_clinic(clinicName):
#     if (Clinic.query.filter_by(clinicName=clinicName).first()):
#         return jsonify({"message": "Clinic '{}' already exists.".format(clinicName)}), 400
 
#     data = request.get_json()
#     clinic = Clinic(clinicName, **data)
 
#     try:
#         db.session.add(clinic)
#         db.session.commit()
#     except:
#         return jsonify({"message": "An error occurred creating the clinic."}), 500
 
#     return jsonify(clinic.json()), 201

# Create doctor in clinic
# @app.route("/clinic/<string:doctorName>", methods=['POST'])
# def create_doctor(clinicName, doctorName):
#     if (Clinic.query.filter(clinicName=clinicName).filter(doctorName=doctorName).first()):
#         return jsonify({"message": "Doctor '{doctorName}' already exists in Clinic '{clinicName}.".format(doctorName, clinicName)}), 400
 
#     data = request.get_json()
#     clinic = Clinic(clinicName, **data)
 
#     try:
#         db.session.add(clinic)
#         db.session.commit()
#     except:
#         return jsonify({"message": "An error occurred adding the doctor to the clinic."}), 500
 
#     return jsonify(clinic.json()), 201

if __name__ == '__main__': # if it is the main program you run, then start flask
    # with docker
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(port=5000, debug=True) #to allow the file to be named other stuff apart from app.py
    # debug=True; shows the error and it will auto restart
