import sublime, sublime_plugin

class OosCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		className = self.view.substr(sels[0]);

		for sel in sels:

			if(self.view.substr(sel)!=className):
				selectedText = self.view.substr(sel)
				capitalizedText = selectedText[0].title() + selectedText[1:]

				setter = "\n"+className + ".prototype.set"+capitalizedText+"= function("+selectedText+"){\n\tthis."+selectedText+" = "+selectedText+";\n};\n"

				self.view.insert(edit, self.view.size(), setter);
				setter ="";
