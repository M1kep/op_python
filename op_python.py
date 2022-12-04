import subprocess

from typing import List


class CLI:
    def __init__(self, op_path=None):
        self.op_path = op_path

    def execute(self, cmd: List[str]):
        full_command = []
        if self.op_path is not None:
            full_command.append(f'{self.op_path}')
        else:
            full_command.append("op")

        full_command = list(full_command + cmd)
        return subprocess.run(full_command, capture_output=True)

    def read(self, ref):
        return self.execute(["read", ref]).stdout.decode()
