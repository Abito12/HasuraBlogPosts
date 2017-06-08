import os

blogID = []

for file in os.listdir():
    if file[-4:] == "html":
        currentID = int(file[12]);
        blogID.append(currentID);
if len(blogID)!=0:
    newID = int (max(blogID)) + 1
else:
    newID = 1

heading = input("Enter blog heading: " )
author  = "Abito Prakash"
date = input("Date: ")
content = input("Content: ")

template = """<html>
<head>
  <meta charset="UTF-8">
  <title>Article | Blog App</title>
     <link rel="icon" href="https://juststickers.in/wp-content/uploads/2016/09/lamda.png">
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
  <link href='https://fonts.googleapis.com/css?family=Varela+Round' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Monoton' rel='stylesheet' type='text/css'>
<link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css'>
<link rel="stylesheet" href="articlePage.css">
<link href="https://afeld.github.io/emoji-css/emoji.css" rel="stylesheet">
<script src="articlePage.js"></script>


</head>

<body>
 <div class="container">
 <div class="content">
	<h1>%s</h1>
	<h6>Written By %s
    <span>%s</span></h6>
	<p>%s</p>

</div>
</div>
</div>
</div>
</body>
</html>""" % (heading,author,date, content)

newBlogPost = "BlogPostWeek" + str(newID) + ".html"

fw = open(newBlogPost, 'w');
fw.write(template);
fw.close()

input("Press <enter> to exit")