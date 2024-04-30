from pathlib import Path
from datetime import datetime
from abc import ABC, abstractmethod
from contextlib import contextmanager
import json
from string import Template


log_template = '$user logged at system $time'

class GetData(ABC):
    def __init__(self, user, password, data):
        self.data = data
        self.log_template = log_template
        self.user = user
        self.password = password


    @abstractmethod
    def send_log(self):
        my_template = Template(log_template)
        my_template.substitute(user=)