from bottle import route, run, request, abort


@route('/containers/', method='GET')
def list_containers():
    print('Listing containers.')


@route('/containers', method='PUT')
def create_container():
    data = request.json
    if not data:
        abort(400, 'No data received')
    print ('Creating container using the following data: %s' % data)


@route('/containers/:name', method='DELETE')
def delete_container(name):
    print('Killing container %s.' % name)


run(host='localhost', port=8080)
