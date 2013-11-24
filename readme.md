# OOJS - Sublime Text plugin

*Sublime Text Plugin to generate Get/Set methods*

> [OOJS](https://github.com/avenauche/OOJS) helps developers to generate Getters and Setters in Object Oriented JavaScript fashion. This plugin is an enhanced version of existing *proto* snippet.

## Install

Install `OOJS` with [Package Control](https://sublime.wbond.net) and restart Sublime.


## Getting started

### Example 

```ini
# example.js

var exampleNode = function(){
	this.prop1;
	this.prop2;
	this.prop3;
};

/*In this case, the generated code will look like the following*/

exampleNode.prototype.getProp1 = function(){
	return this.prop1;
};

exampleNode.prototype.setProp1(prop1){
	this.prop1 = prop1;	
};

```


## Tips

### Keyboard Shortcuts

*ctrl+alt+z* will generate the getter and setter for all selected properties.

*ctrl+alt+g* will generate the getter for all selected properties.

*ctrl+alt+s* will generate the setter for all selected properties.

### Access using Menubar

Select the required properties and then choose

1. Edit -> OOJS -> OOGS (Getter + Setter)
2. Edit -> OOJS -> OOG (Getter)
3. Edit -> OOJS -> OOS (Setter)


### Access using Context Menu

Select the required properties and then  right click and choose

1. OO Getter Setter 
2. OO Getter
3. OO Setter


### Access using Sidebar Menu

Select the required properties and then right click on the filename in the sidebar and choose

1. OO Getter Setter 
2. OO Getter
3. OO Setter

## License

MIT License • © [Avinash Jayakumar](mailto:avenauchejeyasooriya@gmail.com)