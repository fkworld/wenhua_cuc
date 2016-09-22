from modelsAdmin import Admin
from modelsArticle import Article
from formsArticle import ArticleForm
from formsAdmin import LoginForm
from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint
from flask_login import login_user,logout_user,login_required,current_user
from main import db,login_manager

views_blueprint=Blueprint('views_blueprint',__name__)

@views_blueprint.route('/',methods=['GET','POST'])
def index():
    articles=Article.query.all()
    articles.reverse()
    return render_template('index.html',articles=articles)

@views_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@views_blueprint.route('/login',methods=['GET','POST'])
def login():
    login=LoginForm()
    if login.validate_on_submit():
        answer=login.answer.data
        if login.verify_answer(login.answer.data):
            admin=Admin()
            login_user(admin,login.remember_me.data)
            flash('管理员账户登录成功！')
            return redirect(request.args.get('next') or url_for('views_blueprint.index'))
        flash('口令错误！')
    return render_template('login.html',form=login)

@views_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('管理员账户登出！')
    return redirect(url_for('views_blueprint.index'))

@views_blueprint.route('/new_article',methods=['GET','POST'])
@login_required
def new_article():
    form=ArticleForm()
    if form.validate_on_submit():
        article=Article()
        article.set_all_by_form_6_values(form)
        article.update_db()
        flash('文章提交成功')
        return redirect(url_for('views_blueprint.article',tag_id=article.tag_id,article_id=article.id))
    return render_template('new_article.html',form=form)

@views_blueprint.route('/edit_article/<article_id>',methods=['GET','POST'])
@login_required
def edit_article(article_id):
    article=Article.query.get_or_404(article_id)
    form=ArticleForm()
    if form.validate_on_submit():
        article.set_all_by_form_6_values(form)
        article.update_db()
        flash('文章已更新成功')
        return redirect(url_for('views_blueprint.article',tag_id=article.tag_id,article_id=article.id))
    form.set_form_data(article)
    return render_template('edit_article.html',form=form)

@views_blueprint.route('/delete_article/<article_id>',methods=['GET','POST'])
def delete_article(article_id):
    article=Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    flash('文章删除成功')
    return redirect(url_for('views_blueprint.show_articles'))

@views_blueprint.route('/show_articles')
@login_required
def show_articles():
    articles=Article.query.all()
    articles.reverse()
    return render_template('article_list.html',articles=articles)

@views_blueprint.route('/article/contact_us')
def contact_us():
    article=Article.query.get_or_404(1)
    return render_template('article.html',article=article)

@views_blueprint.route('/article/version')
def version():
    article=Article.query.get_or_404(2)
    return render_template('article.html',article=article)


@views_blueprint.route('/article/<tag_id>/<article_id>')
def article(tag_id,article_id):
    article=Article.query.get_or_404(article_id)
    return render_template('article.html',article=article)

@views_blueprint.route('/article/<tag_id>/')
def show_article_by_tag(tag_id):
    articles=Article.query.filter_by(tag_id=tag_id)
    return render_template('index.html',articles=articles)


@views_blueprint.route('/_test',methods=['GET','POST'])
def _test():
    form=LoginForm()
    if form.validate_on_submit():
        admin=Admin()
        admin.account=form.account.data
        admin.set_password_hash(form.password.data)
        db.session.add(admin)
        db.session.commit()
    return render_template('login.html',form=form)