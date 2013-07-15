from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form
from appstore.models import Post, User

from forms import AddAppForm, LoginForm, RegisterForm

posts = Blueprint('posts', __name__, template_folder='templates')



class Index(MethodView):

    def get(self):
        # posts = Post.objects.all()
        login = LoginForm()
        # register = RegisterForm()
        # form = {"login":login, "reg":register}
        return render_template('index.html', login = login)

    def post(self):

        form = LoginForm(request.form)
        print form.name.data
        login = LoginForm()
        return render_template('index.html', login = login)

class Addapp(MethodView):

    def get(self):
        form = AddAppForm()
        return render_template('add/addapp.html', form = form)

    def post(self):
        form = AddAppForm(request.form)
        if form.validate():
            post = Post()
            post.name = form.name.data
            post.category = form.category.data
            post.description = form.description.data
            post.save()
            return redirect('/')

        form = AddAppForm()
        return render_template('add/addapp.html', form = form)


# class Login(MethodView):
#     def get(self):
#         # posts = Post.objects.all()
#         form = LoginForm()
#         return render_template('login/login.html', form = form)
#     def post(self):
#         form = LoginForm(request.form)

class Register(MethodView):
    def get(self):
        register = RegisterForm()
        return render_template('register/register.html', register = register)

    def post(self):
        print 'registering...'
        register = RegisterForm(request.form)
        print 'register.name.data ', register.name.data
        if register.validate():
            print 'valid'
            user = User()
            user.name = register.name.data
            user.password = register.password.data
            user.email = register.email.data
            # user.save()
            return redirect('welcome/')

        register = RegisterForm()
        return render_template('register/register.html', register = register)    
        # return redirect('welcome.html')    

class Welcome(MethodView):
    def get(self):
        return render_template('welcome/welcome.html')





# Register the urls
posts.add_url_rule('/', view_func=Index.as_view('index'))
posts.add_url_rule('/welcome/', view_func=Welcome.as_view('welcome'))
posts.add_url_rule('/register/', view_func=Register.as_view('register'))
posts.add_url_rule('/add/', view_func=Addapp.as_view('addapp'))
# posts.add_url_rule('/login/', view_func=Login.as_view('login'))
