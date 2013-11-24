import sublime, sublime_plugin

class OogsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel();
		className = self.view.substr(sels[0]);

		for sel in sels:

			if(self.view.substr(sel)!=className):
				selectedText = self.view.substr(sel)
				capitalizedText = selectedText[0].title() + selectedText[1:]

				getter = "\n"+className + ".prototype.get"+capitalizedText+"= function(){\n\treturn this."+selectedText+";\n};\n"
				setter = "\n"+className + ".prototype.set"+capitalizedText+"= function("+selectedText+"){\n\tthis."+selectedText+" = "+selectedText+";\n};\n"

				self.view.insert(edit, self.view.size(), getter+setter);
				getter = ""; setter ="";
