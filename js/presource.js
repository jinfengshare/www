// to degbug it, use alert !
window.onload = function()
{
	var pre = document.getElementsByTagName("pre");
	for(var i=0; i<pre.length; i++)
	{
		// get data from pre section
		var target=pre.item(i);
		if("source" != target.className)
			continue;
		var content = target.firstChild.nodeValue;
		// split by <cr> - one line
		var linesArray = content.split(String.fromCharCode(13));
		if(1 == linesArray.length)
			linesArray = content.split(String.fromCharCode(10));
		
		// construct pre-ol section
		var ol_container = document.createElement("ol");
		// I'm not sure expr[len-1] is correct, as newer to js
		for(var j=0; j<linesArray.length-1; j++)
		{
			var li_container = document.createElement("li");
			//var span_container = document.createElement("span");
			var text = document.createTextNode(linesArray[j]);
			//span_container.appendChild(text);
			//li_container.appendChild(span_container);
			li_container.appendChild(text);
			ol_container.appendChild(li_container);
		}

		while(target.firstChild)
			target.removeChild(target.firstChild);

		target.appendChild(ol_container);
	}
}
