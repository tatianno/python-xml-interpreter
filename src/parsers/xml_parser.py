from xml.etree import ElementTree
from elements import StartEvent, EndEvent, SequenceFlow, ExclusiveGateway, Task
from processes import MainProcess


class XmlParser:

    def __init__(self, path: str) -> None:
        self._path = path
        self._tree = ElementTree.parse(path)
        self._root = self._tree.getroot()
        self._namespaces = {'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'}
        self._process = self._root.find('.//bpmn:process', namespaces=self._namespaces)
    
    def get_main_process(self) -> MainProcess:
        return MainProcess(**self._process.attrib)
    
    def get_start_event(self) -> StartEvent:
        start_event = self._process.find('.//bpmn:startEvent', namespaces=self._namespaces)
        return StartEvent(**start_event.attrib)
    
    def get_end_event(self) -> EndEvent:
        end_event = self._process.find('.//bpmn:endEvent', namespaces=self._namespaces)
        return EndEvent(**end_event.attrib)
    
    def get_sequences_flows(self) -> list[SequenceFlow]:
        return [
            SequenceFlow(**sequence_flow.attrib)
            for sequence_flow in self._process.findall(
                './/bpmn:sequenceFlow'
                , namespaces=self._namespaces
            )
        ]
    
    def get_exclusives_gateways(self) -> list[ExclusiveGateway]:
        return [
            ExclusiveGateway(**exclusive_gateway.attrib)
            for exclusive_gateway in self._process.findall(
                './/bpmn:exclusiveGateway'
                , namespaces=self._namespaces
            )
        ]
    
    def get_tasks(self) -> list[Task]:
        return [
            Task(**task.attrib)
            for task in self._process.findall(
                './/bpmn:task'
                , namespaces=self._namespaces
            )
        ]