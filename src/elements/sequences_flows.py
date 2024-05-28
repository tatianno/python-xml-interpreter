class SequenceFlow:
    
    def __init__(self, id: str, sourceRef: str, targetRef: str, name: str=None, *args, **kwargs):
        self.id = id
        self._source_id = sourceRef
        self._target_id = targetRef
        self._name = name