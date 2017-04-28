from modelsArticle import Article

if __name__=='__main__':
    article = Article()
    article_list = article.search_all()
    print(article_list)