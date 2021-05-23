from service.api.wework_api import WeWork


class Tag(WeWork):
    def add(self, name):
        data = {

        }
        return self.request(data)

    def search(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
