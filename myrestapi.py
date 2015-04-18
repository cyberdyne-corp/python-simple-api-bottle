from bottle import route, run, request, abort


class ContainerManager:

    def list_containers():
        print('Listing containers')

    def create_container(data):
        print('Creating container using the following data: %s' % data)

    def delete_container(name):
        print('Killing container %s.' % name)

manager = ContainerManager


@route('/containers/', method='GET')
def list():
    manager.list_containers()


@route('/containers/', method='POST')
def create():
    data = request.json
    if not data:
        abort(400, 'No data received')
    manager.create_container(data)


@route('/containers/:name', method='DELETE')
def delete(name):
    manager.delete_container(name)

run(host='localhost', port=8080)
