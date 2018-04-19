import falcon
import json

class user_controller:
    def on_get(self, req, resp):
        resp.body = json.dumps({
            "message": "User modules is running successfully."
        }, ensure_ascii=False)
        resp.status = falcon.HTTP_200
