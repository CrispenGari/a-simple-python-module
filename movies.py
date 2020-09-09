import requests
from enum import Enum
class HttpError(Exception):
    pass
class Http404(Exception):
    pass
class ErrorStrings(Enum):
    not_found = "ERROR 404 NOT FOUND",
    bad_request = "HTTP BAD REQUEST"
    pass
class Movies:
    def __init__(self):
        pass
    def get_movies_or_404(self, API_KEY, query_string):
        base_url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query={}&api-key={}".format(query_string,
                                                                                                          API_KEY)
        error_object = ErrorStrings
        try:
            raw_data = requests.get(base_url)
            if (raw_data.status_code == 200):
                try:
                    if(raw_data.json()['num_results'] == 0):
                        raise Http404(error_object.not_found.value[0])
                    else:
                        return  raw_data.json()
                except Http404 as e:
                    print(e)
                finally:
                    pass
            else:
                raise HttpError(error_object.bad_request.value[0])
        except HttpError as error:
            print(error)
        finally:
            pass
    pass
pass

