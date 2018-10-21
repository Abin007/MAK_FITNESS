from flask import Flask,render_template,request,url_for,redirect
import pandas as pd 
import xlsxwriter as xlsw
import math
from datetime import date
import os
import csv

app = Flask(__name__)
total=[]
Cusomer_info=[]
reg_number=430
reg_number_write=[]
rc=0
i=0
@app.route('/', methods=['GET', 'POST'])
def hello_world():
	rc = os.open('reg_num.txt',os.O_CREAT|os.O_RDWR|os.O_APPEND,0777)
	temp = os.popen('tail -n 1 reg_num.txt').read().split('\n')
	return render_template('MAK_fitness.html', reg_num=temp)

# @app.route('/words/<wor>',methods=['GET', 'POST'])
# def hello(wor):
# 	print"tell me something"
# 	print wor
# 	return render_template('track.html',word=wor)

@app.route('/login', methods=['POST','GET'])
def form_data():
	info=[]
	training=[]
	global total
	firstname = request.form['firstname']
	info.append(firstname)
	middlename = request.form['middlename']
	info.append(middlename)
	lastname = request.form['lastname']
	info.append(lastname)
	address = request.form['address']
	info.append(address)
	phone = request.form['phone']
	info.append(phone)
	dob = request.form['dob']
	info.append(dob)
	occup = request.form['occup']
	info.append(occup)
	email = request.form['email']
	info.append(email)
	gender = request.form['gender']
	info.append(gender)
	age = request.form['age']
	info.append(age)
	heigth = request.form['Heigth']
	info.append(heigth)
	weigth = request.form['Weigth']
	info.append(weigth)
	bg = request.form['bg']
	info.append(bg)
	hp = request.form['hp']
	info.append(hp)
	training=request.form.getlist('training')
	training=[str(i) for i in training]
	info = [str(i) for i in info]
	total=info+training
	return render_template('confirmation.html',total=total)

@app.route("/confirm",methods=['POST','GET'])
def confirm():
	global reg_number
	global rc
	global Cusomer_info
	global i
	rc = os.open('reg_num.txt',os.O_CREAT|os.O_RDWR|os.O_APPEND,0777)
	temp=os.popen('tail -n 1 reg_num.txt').read().split('\n')
	reg_number=int(temp[0])
	workbook = xlsw.Workbook('Customer.xlsx')
	Cusomer_info.append(reg_number)
	Cusomer_info=Cusomer_info + total
	print Cusomer_info
	df = pd.DataFrame(Cusomer_info)
	df = df.transpose()
	xlsfile = 'Customer.xlsx'
	writer = pd.ExcelWriter(xlsfile, engine='xlsxwriter')
	i=2
	df.to_excel(writer, sheet_name="Sheet1",startrow=i, startcol=1, header=False, index=False)
	writer.save()
	writer.close()
	i=i+1

	with open('Customer','a') as customer:
		wr=csv.writer(customer, dialect='excel')
		wr.writerow(Cusomer_info)
	del Cusomer_info[:]




	reg_number=reg_number +1
	reg_number_var = os.write(rc,str(reg_number)+'\n')
	temp = os.popen('tail -n 1 reg_num.txt').read().split('\n')
	return render_template('MAK_fitness.html',reg_num=temp)


if __name__ == '__main__':
	app.run(debug = True)
