from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint
from flask_login import login_user,logout_user,login_required,current_user

from start import login_manager
from modelsAdmin import Admin
from modelsArticle import Article
from forms import ArticleForm,LoginForm

views_blueprint = Blueprint('views_blueprint', __name__)


@views_blueprint.route('/',methods=['GET','POST'])
def index():
    article = Article()
    article_list = article.search_all()
    article_list.reverse() # 排序
    return render_template('index.html', article_list=article_list, page_title='INDEX')

@views_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@views_blueprint.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        admin = Admin()
        login_list = [login_form.account.data, login_form.password.data]
        if admin.verify_login(login_list):
            login_user(admin, login_form.remember_me.data)
            flash('管理员账户登录成功！')
            print('Login sucess.')
            return redirect(request.args.get('next') or url_for('views_blueprint.index'))
        else:
            flash('管理员账户登录失败，请检查账户密码是否正确！')
    return render_template('login.html', form=login_form, page_title='ADMIN LOGIN')

@views_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('管理员账户登出！')
    return redirect(url_for('views_blueprint.index'))

@views_blueprint.route('/new_article',methods=['GET','POST'])
@login_required
def new_article():
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        article = Article()
        article.form_to_object(article_form)
        article.new_article()
        flash('文章提交成功')
        return redirect(url_for('views_blueprint.get_article_by_id',article_id=article.id))
    return render_template('edit_article.html', form=article_form, page_title='NEW ARTICLE')

@views_blueprint.route('/edit_article/<article_id>',methods=['GET','POST'])
@login_required
def edit_article(article_id):
    article = Article()
    article.search_by_id(article_id)
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        article.form_to_object(article_form)
        article.update_article()
        flash('文章更新成功')
        return redirect(url_for('views_blueprint.get_article_by_id',article_id=article.id))
    article_form.object_to_form(article) # ??此行语句位置对功能实现有重大影响
    return render_template('edit_article.html', form=article_form, page_title='EDIT ARTICLE')

@views_blueprint.route('/delete_article/<article_id>',methods=['GET','POST'])
@login_required
def delete_article(article_id):
    article = Article()
    article.search_by_id(article_id)
    message = article.delete_article()
    flash(message)
    return redirect(url_for('views_blueprint.show_article_list'))

@views_blueprint.route('/show_article_list')
@login_required
def show_article_list():
    article = Article()
    article_list = article.search_all()
    return render_template('article_list.html', article_list=article_list, page_title='ARTICLE LIST')

@views_blueprint.route('/article/website_info')
def website_info():
    article = Article()
    article.search_by_id(1)
    return render_template('article.html', article=article)

@views_blueprint.route('/article/update_info')
def update_info():
    article = Article()
    article.search_by_id(2)
    return render_template('article.html', article=article)

@views_blueprint.route('/article/<article_id>')
def get_article_by_id(article_id):
    article = Article()
    article.search_by_id(article_id)
    return render_template('article.html', article=article)

@views_blueprint.route('/article_list/<article_tag>')
def get_article_list_by_tag(article_tag):
    article = Article()
    article_list = article.search_by_tag(article_tag)
    return render_template('article_list.html', article_list=article_list, page_title=article_tag)

@views_blueprint.route('/_test',methods=['GET','POST'])
def _test():
    return render_template('bootstrap.html')
