import web

urls = ('/upload', 'Upload',
        '/thanks', 'Thanks')

render = web.template.render("templates/", base="layout")

class Thanks(object):
    def GET(self):
        return render.thanks()

class Upload(object):
    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        return render.upload()

    def POST(self):
        x = web.input(myfile={})
        filedir = "/mnt/c/Users/arjun/Desktop/Arjun/School/Courses/Projects/Python/fileupload/upload"
        if 'myfile' in x:
            filepath = x.myfile.filename.replace('\\','/')
            filename = filepath.split('/')[-1]
            fout = open(filedir + '/'+filename, 'wb')
            fout.write(x.myfile.file.read())
            fout.close()
            raise web.seeother('/thanks')
        else:
            raise web.seeother('/upload')
    

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
