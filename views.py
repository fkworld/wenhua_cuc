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
    return render_template('index.html', article_list=article_list)

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
    return render_template('login.html', form=login_form)

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
        article.new_article(article_form)
        flash('文章提交成功')
        return redirect(url_for('views_blueprint.get_article_by_id',article_id=article.id))
    return render_template('new_article.html',form=article_form)

@views_blueprint.route('/edit_article/<article_id>',methods=['GET','POST'])
@login_required
def edit_article(article_id):
    article=Article.query.get_or_404(article_id)
    form=ArticleForm()
    if form.validate_on_submit():
        article.set_all_by_form_6_values(form)
        article.update_db()
        flash('文章已更新成功')
        return redirect(url_for('views_blueprint.get_article',article_id=article.id))
    form.set_form_data(article)
    return render_template('edit_article.html',form=form)

@views_blueprint.route('/delete_article/<article_id>',methods=['GET','POST'])
def delete_article(article_id):
    article=Article.query.get_or_404(article_id)
    message=article.delete()
    flash(message)
    return redirect(url_for('views_blueprint.show_articles'))

@views_blueprint.route('/show_articles')
@login_required
def show_articles():
    articles = Article.query.all()
    articles.reverse()
    return render_template('articles.html',articles=articles)

@views_blueprint.route('/article/website_info')
def website_info():
    article=Article.query.get_or_404(20161107154545)
    #基础文件：网站说明，数据库写死，目前ID：20161107154545
    return render_template('article.html',article=article)

@views_blueprint.route('/article/update_info')
def update_info():
    article=Article.query.get_or_404(20161107154806)
    #基础文件：更新公告，数据库写死，目前ID：20161107154806
    return render_template('article.html',article=article)

@views_blueprint.route('/article/<article_id>')
def get_article_by_id(article_id):
    article = Article()
    article.search_by_id(article_id)
    return render_template('article.html', article=article)

@views_blueprint.route('/article/<article_tag>')
def get_article_list_by_tag(article_tag):
    article = Article()
    article_list = article.search_by_tag(article_tag)
    return render_template('article_list.html', article_list=article_list)

@views_blueprint.route('/_test',methods=['GET','POST'])
def _test():
    return render_template('bootstrap.html')
