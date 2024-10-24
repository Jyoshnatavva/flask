from flask import Flask,render_template,redirect,url_for,request,flash 
from flask_login import LoginManager,userMixin,login_user,login_required,login_,
app=Flask(_name__)
app.config['SECRET_KEY']='your_secret_key'
login_manager=LoginManager()
login_manager.int_app(app)
login_manager.login_view='login'
users={'user 1':{'password' : 'password123'}} 
class user(usermixin):
    def __init__(self,id):
        self.id=id
        @login_manager.user_loader 
        def load_user(user_id):
            return user(user_id) if user_id in users else None
        @app.router('/')
        @login_required 
        def home():
            return render_template('home.html',name=current_user.id)
@app.route('/login',methods=['GET','POST'])
def login()
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username]['password'] == password:
            user =user (username)
            login_user(user)
            return redirect(url_for('home'))
        else:
            flask('Invalid username or password')
            return redirect(url_for('login'))
return render_template('login.html') 
@app.router('/logout')
@login_retuired
def logout():
    logout_user()
    return redirect(url_for('login'))
if _name__=='__main__':
    app.run(debug=true)               