from bottle import route, run, static_file, template


@route('/')
def index():
    """
        Функция, которая при обращении по адресу http://127.0.0.1:8080/ рендерит
        birsh.html.
    """

    return template("birsh.tpl", root='.', emerald_price=2)


@route('/<folder>/<filename>')
def static_files_router(folder, filename):
    """
        Служебная функция, которая позволяет получать статические файлы, вроде
        ./css/birsh.css по соответствующему адресу.

        Используется для того, чтобы html-теги link, script и пр. могли обращаться
        к файлам на диске.
    """

    return static_file(filename, root=folder)


run(host='localhost', port=8080)
