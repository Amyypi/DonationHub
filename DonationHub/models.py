from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Table of users
class users(db.Model):
	username = db.Column(db.String(50), primary_key=True)
	password = db.Column(db.String(50))
	email = db.Column(db.String(50))

class charities(db.Model):
	STATEID = db.Column((db.Integer), primary_key=True)
	ORGID = db.Column(db.Integer)
	ORGANIZATION_NAME = db.Column(db.Text)

class counties(db.Model):
	STATEID = db.Column((db.Integer), db.ForeignKey('states.STATEID'))
	COUNTYID = db.Column((db.Integer), primary_key=True)
	COUNTYNAME = db.Column(db.Text)
	COUNTYPOP = db.Column(db.Integer)

class poverty(db.Model):
	COUNTYID = db.Column((db.Integer), db.ForeignKey('counties.COUNTYID'), primary_key=True)
	POVERTY_ESTIMATE = db.Column(db.Integer)

class states(db.Model):
	STATEID = db.Column((db.Integer), primary_key=True)
	STATENAME = db.Column(db.Text)
	ABBREVIATION = db.Column(db.Text)
	STATEPOP = db.Column(db.Integer)

class unemployment(db.Model):
	COUNTYID = db.Column((db.Integer), db.ForeignKey('counties.COUNTYID'), primary_key=True)
	UNEMPLOYED_PEOPLE = db.Column(db.Integer)
	UNEMPLOYMENT_RATE = db.Column(db.Integer)

	def to_dict(self):
		return {
        'COUNTYID': self.COUNTYID,
        'UNEMPLOYED_PEOPLE': self.UNEMPLOYED_PEOPLE,
        'UNEMPLOYMENT_RATE': self.UNEMPLOYMENT_RATE,
    	}
	

## You can also do this in routes.py within specific functions. but just for easier view - I wrote this down here: 

##########  Unemployment ########## 
#unemployment_result = db.session.query(unemployment, counties).join(counties).all()
# print all the info needed for Table of unemployment 
# for unemployment, counties in unemployment_result:
#	print(unemployment.COUNTYID, counties.COUNTYNAME, unemployment.UNEMPLOYED_PEOPLE)

######### only prints out the matching countyIDs, but you can see how it matches the two tables together
#print(unemployment_result)

####################################################################

##########  Population ########## 
#state_county_result = db.session.query(states,counties).join(counties).all()
# print all the info needed for Table of Population 
#for states, counties in state_county_result:
#	print(states.STATEID, states.STATENAME, states.ABBREVIATION, "State-population:", states.STATEPOP, "County-FIPS:", counties.COUNTYID, counties.COUNTYNAME, "County-population:",counties.COUNTYPOP)

#all_table_result = db.session.query(states, counties, unemployment, poverty).join(counties).join(unemployment).join(poverty).all()
#for states, counties, unemployment, poverty in all_table_result:
#	print(states.STATEID, states.STATENAME, states.ABBREVIATION, states.STATEPOP, counties.COUNTYID, counties.COUNTYNAME, counties.COUNTYPOP, unemployment.UNEMPLOYED_PEOPLE, unemployment.UNEMPLOYMENT_RATE, poverty.POVERTY_ESTIMATE)

