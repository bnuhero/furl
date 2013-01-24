# furl
furl is a [python][1] program to find urls of the video and slides(or transcripts) in an [InfoQ][2] presentation(or interview) web page.

To run furl, you will need to [obtain and install python][3] 2.6-2.7, if not already on your system. 

## 1. Usage
By default, furl is very simple to invoke. The basic syntax is:

	python /path/to/furl/furl.py [-p server:port] <url>

Options begin with a dash and consist of a single letter. The following is a list of options when running furl from the command line. 

+ -p: Specific the http proxy server address and port number. For example, 

> -p 127.0.0.1:8080

Any additional arguments on command line are normally treated as the URL of an InfoQ presentation(or interview) web page.

## 2. Example

### 2.1 InfoQ Presentation
For [this presentation][4] with the title **"Architecture of a Modern Web App"**, run furl from command prompt:

	$ python /path/to/furl/furl.py http://www.infoq.com/presentations/Web-App-Meteor-Derby

All found urls will be listed in the command window:
> http://d1snlc0orfrhj.cloudfront.net/presentations/12-oct-archofamodernwebapp.mp4  
> http://www.infoq.com/resource/presentations/Web-App-Meteor-Derby/en/slides/sl1.jpg  
> http://www.infoq.com/resource/presentations/Web-App-Meteor-Derby/en/slides/sl2.jpg  
> ...  
> http://www.infoq.com/resource/presentations/Web-App-Meteor-Derby/en/slides/sl31.jpg

What's next? A new file with the name **"player.html"** should be created in current directory. Browse it for more information. 

### 2.2 InfoQ Interview
For [this interview][5] with the title **"End-to-end JavaScript Development with Juergen Fesslmeier"**, run furl from command prompt:

	$ python /path/to/furl/furl.py http://www.infoq.com/interviews/end-to-end-javascript

The video url will be listed in the command window:
> http://d1snlc0orfrhj.cloudfront.net/interviews/12-nov-juergen-fesslmeier.mp4

What's next? A new file with the name **"player.html"** should be created in current directory. Browse it for more information. 

## 3. License
Source code released under [the MIT License][6].

(c) 2013, I.O. Studio, Guangzhou, China.

[1]: http://www.python.org/
[2]: http://www.infoq.com/
[3]: http://www.python.org/download/
[4]: http://www.infoq.com/presentations/Web-App-Meteor-Derby
[5]: http://www.infoq.com/interviews/end-to-end-javascript
[6]: http://www.opensource.org/licenses/mit-license.php