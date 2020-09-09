'''
    CODERS:          CRISPEN && BONGA
    DESCRIPTION:     GETTING HTTP REQUEST USING THE REQUESTS MODULE IN PYTHON
                     [CREATING AN EXTERNAL MODULE IN PYTHON]
                     THIS MODULE WILL ALLOW US TO GET MOVIES INFOMATION FROM AN
                     API

'''
API_KEY = "API_KEY"
QUERY_STRING ="gamers"
from movies import  Movies
if(Movies.get_movies_or_404("", API_KEY, QUERY_STRING) == None or "" ):
    pass
else:
    print(Movies.get_movies_or_404("", API_KEY, QUERY_STRING))
