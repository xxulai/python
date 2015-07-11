#-*-coding :utf-8-*-
import web
from gothonweb import map

urls = (
	'/game', 'GameEngine',
	'/', 'Index'
)

'''
if in this way
urls = (
	'/game', 'GameEngine' !!!!!!!!!!!! no ',' here, there will be 1 object missing!!!!! then will keep reporting --> ValueError: need more than 1 value to unpack
	'/', 'Index'
)
'''

app=web.application(urls, globals())

#hack to make debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room':None})
	web.config._session = session
else:
	session = web.config._session
	
render = web.template.render('templates/', base='layout') #use the template templates/layout.html

class Index(object):

	def GET(self):
		#this is used to "setup" the session with starting values
		session.room = map.START
		web.seeother("/game")
		
class GameEngine(object):
	
		def GET(self):
			if session.room:
				return render.show_room(room=session.room)
			else:
				return render.you_died()
		
		def POST(self):
			form = web.input(action=None)
			
			if session.room and form.action:
				session.room = session.room.go(form.action)

			web.seeother("/game")
			
if __name__ == "__main__":
	app.run()