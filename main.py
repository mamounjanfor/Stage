# to open/create a new html file in the write mode
import codecs
import webbrowser
f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
html_template = """
<html>
<head></head>
<body>
<p>Hello World! </p>

</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()

# viewing html files
# below code creates a
# codecs.StreamReaderWriter object
file = codecs.open("GFG.html", 'r', "utf-8")

# using .read method to view the html
# code from our object
print(file.read())
# open html file
webbrowser.open('GFG.html')