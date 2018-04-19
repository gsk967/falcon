import json
import falcon


class Sample(object):
    def on_get(self, req, resp):
        # Create a JSON representation of the resource
        resp.body = json.dumps({
            "message": "Server is running successfully."
        }, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200


def handle_404(req, resp):
    resp.body = json.dumps({"status": "error", "message": "Route not found"})
    resp.status = falcon.HTTP_404

api = application = falcon.API()
api.add_route('/', Sample())

# any other route should be placed before the handle_404 one
api.add_sink(handle_404, '')

# Advanced configurations 
# importing the user module routes add to the falcon
import falcon_sample.modules.users.routes as user_routes
user_routes.add(api)
