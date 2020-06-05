class Filter:
    def __init__(self, objects, filters):
        self.objects = objects
        self.filters = filters

    def apply_filters(self):
        filtered_objects = []
        category = self.filters['category']
        kind = self.filters['kind']
        color = self.filters['color']
        size = self.filters['size']
        for obj in self.objects:
            if (obj.category.name in category or len(category) == 0) and (
                    obj.kind.name in kind or len(kind) == 0):
                for info in obj.information.all():
                    if (info.color.name in color or len(color) == 0) and (
                            info.size.name in size or len(size) == 0):
                        filtered_objects.append(obj)

        return filtered_objects
