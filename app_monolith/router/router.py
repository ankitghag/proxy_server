class crouter:
    def __init__(self, routes):
        self.routes= routes

    def get_upstream_server(self, req_path):
        r= None
        for x in self.routes:
            if req_path.startswith(x.prefix):
                r=x
        return r
