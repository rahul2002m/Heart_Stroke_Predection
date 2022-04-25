from django.shortcuts import render
from flask import Flask,flash, redirect, url_for, request,render_template
from heart_stroke import calc
from bmi import calbmi

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index',methods = ['POST','GET'])
def index():
    res=""
    gj=nw=pr=se=ch=ssu=sfs=sns=sss=0
    if(request.method=='POST'):
        gen = request.form.get('gen')
        age = request.form.get('age')
        ht = request.form.get('ht')
        hd = request.form.get('hd')
        mar = request.form.get('mar')
        rt = request.form.get('rt')
        gl = request.form.get('gl')
        bmi = request.form.get('bmi')
        jt = request.form.get('jt')
        sh = request.form.get('sh')
        if jt=='gj':
            gj=1
        elif jt=='nw':
            nw=1
        elif jt=='pr':
            pr=1
        elif jt=='se':
            se=1
        elif jt=='ch':
            ch=1
        if sh=='ssu':
            ssu=1
        elif sh=='sfs':
            sfs=1
        elif sh=='sss':
            sss=1
        elif sh=='sns':
            sns=1
        x = calc((int(gen), float(age), int(ht), int(hd), int(mar), int(rt), float(gl), float(bmi), int(gj), int(nw), int(pr), int(se), int(ch), int(ssu), int(sfs), int(sns), int(sss)))
        if x==0:
            res="You may not get stroke if you maintain good health :)"
        else:
            res="You may get stroke if you maintain the health !!"
        return render_template('index.html',res=res)
    return render_template('index.html',res="")

@app.route('/bmi',methods = ['POST','GET'])
def bmi():
    if request.method == 'POST':
        h = request.form.get('height')
        w = request.form.get('weight')
        x = calbmi(float(h), float(w))
        s= "BMI of given data = "+str(x)
        return render_template('bmi.html',x=s)

    return render_template('bmi.html')


if __name__ == '__main__':
   app.run(debug = True)