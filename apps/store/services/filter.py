class Filter:
    def __init__(self, objects, filters):
        self.objects = objects
        self.filters = filters

    def __call__(self, *args, **kwargs):
        self.apply_filters()

    def apply_filters(self):
        filtered_objects = []
        for obj in self.objects:
            if obj.category.name in self.filters.category and obj.kind.name in self.filters.kind:
                for info in obj.information:
                    if info.color.name in self.filters.color and info.size.name in self.filters.size:
                        filtered_objects.append(obj)

        return filtered_objects
