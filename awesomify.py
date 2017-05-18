import sublime
import sublime_plugin
import urllib.request, json 


class awesomifycommand(sublime_plugin.TextCommand):
	def run(self, edit):
			view = self.view
			for region in view.sel():
				selection = view.substr(region)
				if selection == '--help':
					with urllib.request.urlopen("http://bunnies.ga/superjson.php") as url:
						data = json.loads(url.read().decode())
						for index in range(len(data)):
							 view.insert(edit,0,data[index]['name']+'\n')
				else:
					with urllib.request.urlopen("http://bunnies.ga/superjson.php") as url:
						data = json.loads(url.read().decode())
						if selection.find('*') != -1:
							getnum = int(selection.split('*')[1])
							if type(getnum) == type(1):
								for index in range(getnum):
									for index in range(len(data)):
										if data[index]['name'] == selection.split('*')[0]:
											view.insert(edit,0,data[index]['content']+'\n\n')
						else:
							for index in range(len(data)):
								if data[index]['name'] == selection:
									view.replace(edit,region,data[index]['content'])
								
				
class awesomifyhelper(sublime_plugin.TextCommand):
	def run(self, edit):
		self.panel = self.view.window().create_output_panel('sf_st3_output')
		self.view.window().run_command('show_panel', { 'panel': 'output.sf_st3_output' })
		self.panel.run_command('awesomifysupercodes')

class awesomifysupercodes(sublime_plugin.TextCommand):
    def run(self, edit):
    	with urllib.request.urlopen("http://bunnies.ga/superjson.php") as url:
    		data = json.loads(url.read().decode())
    		for index in range(len(data)):
    			self.view.insert(edit,self.view.size(),data[index]['name']+'\n')
    	# self.view.insert(edit, self.view.size(), 'hello')