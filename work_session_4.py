import os
import cgi
import urllib

import jinja2

import webapp2
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(autoescape=True, loader = jinja2.FileSystemLoader(template_dir))

#Main page class is for all items on the Home page
class MainPage(webapp2.RequestHandler):
	def get(self):
#The first item in each list is the clickable toggle button, the second is the description		
		template_values={
			'title': 'Intro To {{Programming}}',
			'subheadings':[['Networks', '''<p>A <em>network</em> is a group of entities that can communicate even
			 though they are not all directly connected.  An example would be if two people, such as, Alice and Bob,
			  never directly communicate with each other.  They would only go through Charlie to send messages back 
			  and forth.  So only Charlie would have direct contact to both people.</p>  <p>To make a network there 
			  are a few key things we must know/or have.</p>  <ul> <li>To make a network we need a way to <b>convert</b>
			  messages, <b>encode</b> messages, and <b>interpret</b> messages.</li> <li>We also need to know about 
			  <b>routing</b>.  What's going where.</li>  <li>Who needs to <b>send the message</b> and who gets to 
			  <b>use the resources</b>.</li> </ul>'''],
			['Measuring Networks', '''<p>Latency is the time it takes for messages to get from the source to the 
			  destination.  It's measured in units of time like milliseconds. (1000 milliseconds=1 second)  Bandwidth is 
			  the amount of information that can be transmitted per unit of time and is measured by bits per second.  
			  (MBPS)  A bit is the smalles unit of information.</p> 
			  <div class="main_notes_images"> 
			  <img class="measuring_network_image" src="images/bits_1.png" alt="Drawing illustrating bits"> 
			  <img class="measuring_network_image" src="images/bits_question.png" alt="Question about bits">
			  </div> 
			  <p>In the above example, we see that we want to ask questions that are right 50 percent of the time, 
			  so instead of using 3 questions to find where the star is, we would use 2 to find the answer.</p>'''],
			['HTML Documents', '''<p>For HTML5, to identify which version we are using, we enter the "DOCTYPE" in the first
			 line of our HTML file.  Then we have the HTML tag that surrounds the entire document.  Then we have the head tag 
			 which will contain our javascript, css, or meta data.  The title tag is the title of the document and can be seen 
			 when opened in the browser, at the top of our browser tabs.  And the body tag is where the fun stuff happen!'''],
			['URLS', '''<p>URL stands for <b>Uniform Resource Locator</b>.  In a URL there is the <em>protocol</em>, <em>host</em>,
			  and <em>path</em>.  We can also see <em>query parameters</em> (GET parameters) in our URL.  The "name"= "value of query
			  parameters", the first query is separated with a ?, and the next is separated with &amp;.  <em>Caching</em> stores data
			  so it doesn't need to be retrieved later.  It can be used to make data requests faster.  A <em>fragment</em> is separated
			  fromt he rest of the url with a #.</p>'''],
			['Absolute vs Relative Paths', '''An example of a <em>Relative Path</em> would be a html file (index.html) or a 
			 directory that accesses a file (../graphics/image.png or /help/articles/how-do-i-setup-a-webpage.html).  
			 <em>Absolute Paths</em> are actual websites and will include the actual domain name, as well as http://www...  
			 Relative links only point to a file or a file path.  You must use absolute paths when linking to another website,
			 and though you can also do that within your own website, it is generally frowned upon to do so.  Relative links 
			 make it easy to change your domain name without having to go through all your html pages, hunting down links and 
			 changing the names.  For more information click <a href="http://www.coffeecup.com/help/articles/absolute-vs-relative-pathslinks/">
			 here</a>.</p>'''],
			['HTTP Requests & Responses-& Servers', '''<p>A request line is followed by a number of headers.  Headers have a particular format
			 "name:value".  A <em>Host</em>: "www.example.com"--&gt; This would be the server name. The <em>User Agent</em>: "chrome"--&gt; 
			  The browser.  Web servers can have multiple names.  One machine can host the website for many sites.</p> <p>Other common
			  headers include:</p> <ul> <li>Status line: http/1.1 200ok</li>  <li>Date: Tues Mar 2012 04:33:33 gmt</li> <li>Server: apache/2.2.3</li>
			  <li>Content-Type: tnt/html</li> <li>Content-Length: 1539</li> </ul>  <p>Once browsers make a request 
			  to the server; the server sends a response.  It might respond with a document or information on the document.</p>
			  <div class="main_notes_images"> 
			  <img class="http_image" alt="A drawing showing process and codes of HTTP responses" src="images/http-image.png">
			  </div> 
			  <p>A <em>servers</em> purpose is to respond to HTTP requests.  The computer/browser the person is using sends the request and server responds with usually one of two responses.
			  The first is a <b>static</b> response; which is a pre-written file such as an image.  The second is a <b>dynamic</b> response; which is a program 
			  made "on the fly" called a web application.  It lives on the web server, speaks HTTP, and generates content that your browser requests.</p>'''],
			['Python Break: Modulus and Dictionaries', '''<p>The modulus operator is the percent sign.  A modulus will take a number divided by modulus number
			  and return the <em>remainder</em>.  There is a brief YouTube video that covers Python modulo <a href="https://www.youtube.com/watch?v=b5cb_nfDyyM">
			  here</a>. In Python a Dictionary uses curly braces.  Inside the braces are sets of keys with corresponding values.  Each key can only have one value, 
			  making it a pair.</p> 
			  <div class="main_notes_images"> 
			  <img class="dict_image" alt="A visual showing differences between strings, lists, and dictionaries" src="images/dict-image.png"> 
			  </div>'''],
			  ['Working With Google App Engine & Validation', '''<p>Below is a table illustrating the differences between the "get" method and "post" method.</p>
			   <table border="3" bordercolor="#fdf1f9" cellspacing="5" cellpadding="3">
			   <tr> <td align="center">GET</td> <td align="center">POST</td> </tr>
			   <tr> <td align="center">parameters in URL</td> <td align="center">parameters in body</td> </tr>
			   <tr> <td align="center">used for fetching documents</td> <td align="center">used for updating data</td> </tr>
			   <tr> <td align="center">max URL length</td> <td align="center">no max length</td> </tr>
			   <tr> <td align="center">ok to cache</td> <td align="center">not ok to cache</td> </tr>
			   <tr> <td align="center">shouldn't change server</td> <td align="center">ok to change server</td> </tr>
			   </table>
			   <p>When we begin validation, all we are doing is verifying on the server side that what we expected to receive, is what we actually received.
			   We start by verifying the users input and then, if an error is found, render the form again.  Including an error message will help the user
			   understand what needs to be changed.</p>'''],
			   ['String Substitution, Preserving Input, & HTML Escaping', '''<p>String substitution is where we use the "%"" &"s" together to
			   substitute strings.  It's a place holder for whatever value we are plugging into that spot.  You can sub in one word, or multiple different
			   words, or even a dictionary.</p> <p>We can use string substitution to save a users input.  For instance, instead of using input type="text" value="cool", we can use "%"+(month)+"s".</p> '''],
			   ['HTML Templates', '''<p>In this course we use a template library that is built into Google App Engine, called Jinja2.  In this section we show some of 
			   the ways we can incorporate this into our websites.</p> <div class="html-template-image"> 
			   <figure>
			   <img src="images/variable-substitution.png" alt="Example of variable substitution in Jinja2"> 
			   <img src="images/statement-syntax.png" alt="An image illustrating statement syntax in Jinja2"> 
			   <img src="images/for-loop.png" alt="This is an example of a for loop syntax in Jinja2"> 
			   <img src="images/template-inheritance.png" alt="How template inheritance works">
			   <figcaption>Here are some screen shots showing different syntax used in Jinja2.  From right to left; variable substitution, statement syntax, for loops, and 
			   template inheritance.</figcaption>
			   </figure> </div> <p>Some useful tips when using templates; always automatically escape variables when possible, minimize code in templates, minimize html in code.  
			   If you are like me...when I first was introduced to this, I wondered what the benefits would be of using templates.  To name a few; we can 
			   separate different types of code, our code will be more readable, we'll have more secure websites, and we'll have HTML that is easier to modify.</p>'''],
			   ['Databases & Tables', '''<p>A <em>database</em> is a program that stores and receives large amounts of structured data.
			   A server runs applications and can be used as databases that store and retrieve data.  Typically databases contain one or several tables.
			   Each tbale is identified by a name (e.g. "Customers" or "Orders").  Tables also contain records/rows that include data.  <em>Links</em>
			   are column headings (such as "ID", "Votes", "User", "Title"...).  Every entry of a link is called a row.  There can be many rows for all the links
			   that are submitted.  Every row will have an ID.</p> <div class="table-image">
			   <img src="images/table-image.png" alt="An example of a table in databases."> </div> <p>We can access values in tables using Python, however it is not ideal.
			   It can be error prone, tedious, slow...and just plain difficult.  So to avoid all of that, we can use SQL.</p>'''],
			   ['SQL (aka Structured Query Language)', '''<p><em>SQL</em> allows you to access and manipulate databases.  An example of a SQL query/statement would be,
			   "select * from links where id=5", this statement is saying to fetch data in all columns from the "link" table and then we've applied the constraint, where the ID
			   equals 5.  You could also select a particular column name in a table or list of tables.  There are different operators that can be used in a "where" clause.
			   <a href="http://www.w3schools.com/sql/sql_where.asp">Here</a> is a reference page that touches more on the SQL where clause.  Another thing we can
			   change is the constraint; ID versus submitter.ID.  We can use the "order by" keyword, instead of "where" to sort the result by one of more columns.  SQL joins are
			   a type of query that we can use to involve multiple tables.</p>'''],
			   ['Indexes','''<p>A sequential scan is where we have a list of something and the information gets looped over looking for a
			   particular piece of information.  Indexes make look ups faster.  In python it's similar to dictionaries; indexing a certain
			   location will return that corresponding value.</p>  <div class="index-image">
			   <img src="images/index-image-1.png" alt="Here is an example of using Python dictionaries to map different links based on the lookup information.">
			   <img src="images/index-image-2.png" alt="In this example we have put our function into a variable that can be called in the future and by using the ".get"
			   function, which returns "none" instead of an error.">
			   <img src="images/index-image-3.png" alt="This example uses the existing code to add a new link and index that link to check it's there.">
			   </div>''']]
				}
		template=jinja_env.get_template('webpage_html.html',)

		self.response.out.write(template.render(template_values))#this will render the html page and template values
#The codepen class is for the navigation link to see the embedded codepen page, previous template value needs to be carried over to each page
class codepenHandler(webapp2.RequestHandler):
	def get(self):
		template_values={
			'title': 'Intro To {{Programming}}',
				}

		template=jinja_env.get_template('codepen.html',)

		self.response.out.write(template.render(template_values))

#This general handler code sets up for the jinja template and form/guestbook integration
class myHandler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.write(*a, **kw)

	def render_str(self, template, **params):
		template = jinja_env.get_template(template)
		return template.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template,**kw))


#This code identifies the name of the wall
DEFAULT_WALL='Public'
def wall_key(wall_name=DEFAULT_WALL):
	return ndb.Key('Wall', wall_name)
#This Post class sets up the model for my datastore
class Post(ndb.Model):
	guest_name=ndb.StringProperty(indexed=False)	
	guest_message=ndb.StringProperty(indexed=False)
	date=ndb.DateTimeProperty(auto_now_add=True)
#Guestbook handler holds code for sending and retrieving user input from form to the public guestbook
class guestbookHandler(myHandler):
	def get(self):
		wall_name = self.request.get('wall_name',DEFAULT_WALL)
		if wall_name == DEFAULT_WALL.lower(): wall_name = DEFAULT_WALL
		posts_query = Post.query(ancestor = wall_key(wall_name)).order(-Post.date)
		posts=posts_query.fetch(10)

		template_values={
			'title': 'Intro To {{Programming}}',
				}
	
		template=jinja_env.get_template('guestbook.html')
		guest_name=self.request.get_all("guest_name")
		guest_message=self.request.get_all("guest_message")

		self.response.out.write(template.render(template_values, guest_name=guest_name, guest_message=guest_message))    

	def post(self):
		wall_name = self.request.get('wall_name',DEFAULT_WALL)
        post = Post(parent=wall_key(wall_name))

        guest_message = self.request.get('guest_message')

        if type(guest_message) != unicode:
            post.guest_message = unicode(self.request.get('guest_message'),'utf-8')
        else:
            post.guest_message = self.request.get('guest_message')

        post.put()#writes to the datastore

        query_params = {'wall_name': wall_name}
        self.redirect('/guestbook.html' + urllib.urlencode(query_params))


application=webapp2.WSGIApplication([('/', MainPage),
	('/codepen.html', codepenHandler),
	('/guestbook.html', guestbookHandler)
	], 
	debug=True)
