# sql_injections_detection_flask_api

I have created a simple API in Flask framework that checks if a JSON payload contains characters that could be used to perform SQL injection.
If so, then we get result that input is not sanitized as output.Otherwise,result is sanitized as output.
I have used regular expression indicating common words/characters used in sql queries to access data to find whether given input is SQL injection or not.
