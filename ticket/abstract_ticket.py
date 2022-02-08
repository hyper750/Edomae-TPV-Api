from abc import ABC, abstractmethod

from jinja2 import Environment, FileSystemLoader
from settings import TEMPLATE_DIR


class AbstractTicket(ABC):

    @abstractmethod
    def can_generate_ticket(self, id: int) -> bool:
        pass

    @abstractmethod
    def get_template_name(self) -> str:
        pass

    @abstractmethod
    def get_content(self) -> dict:
        pass

    def get_ticket(self, id: int):
        file_loader = FileSystemLoader(TEMPLATE_DIR)
        env = Environment(loader=file_loader)
        template_content = env.get_template(self.get_template_name())

        return template_content.render(**self.get_content(id))
