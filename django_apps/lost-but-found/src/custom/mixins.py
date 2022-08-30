

class SerializerByMethodMixin:

    def get_serializer_class(self, *args, **kwargs):

        return self.serializer_map.get(self.request.method, self.get_serializer_class)
