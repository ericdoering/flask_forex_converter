### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
- Python uses indentation as part of its syntax
- Javascript is more catered to front end development while python is known to handle back end development
- Python tends to read more like english as opposed to Javascript


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
  for key in dictionary:
  	if key == "c":
  		return True
  		
  return False

	return "c" in dictionary


- What is a unit test?

	A unit test, tests a function in a codebase.

- What is an integration test?

	When you test different pieces together (python->API->Javascript)

- What is the role of web application framework, like Flask?

	Simplifies and handles several aspects of creating a web server with endpoints.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  
  With the query param the user has more influence and flexibility for passing values.

- How do you collect data from a URL placeholder parameter using Flask?

	By using the <"name"> tag within your flask route decorator 
	@app.route("/food/<foodname>")

- How do you collect data from the query string using Flask?

	By using request.args.get('query string key')

- How do you collect data from the body of the request using Flask?

	Depends on the context. Some methods include request.form, request.args, request.json

- What is a cookie and what kinds of things are they commonly used for?

	A way to store data. Cookies can be set to any experation date. Often used for session ID.

- What is the session object in Flask?

	The session object in flask is data held in the server for a particular ID.

- What does Flask's `jsonify()` do?

	jsonify(), serializes flask data into a JSON response.
