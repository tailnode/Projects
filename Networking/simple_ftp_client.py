#!/usr/bin/env python3

from ftplib import FTP
import sys

class FtpClient:
    def __init__(self, host):
        self._ftp = FTP(host)
        self.login()

    def login(self, *param):
        return self._ftp.login()

    def process_cmd(self, cmd):
        options = {
                'cd' : self.change_dir,
                'ls' : self.list_current_dir,
                'login' : self.login,
                'quit' : self.quit,
                'download' : self.download,
                'exit' : self.exit
                }

        cmd = cmd.split()
        result = options[cmd[0]](cmd[1:])
        if result is not None : print(result)

    def change_dir(self, param):
        directory = param[0]
        result = self._ftp.cwd(directory)

    def list_current_dir(self, *param):
        return self._ftp.retrlines('LIST')

    def quit(self, param):
        return self._ftp.quit()

    def exit(self, param):
        sys.exit(0)

    def download(self, param):
        return self._ftp.retrbinary('RETR ' + param[0], open(param[1], 'wb').write)

    def run(self):
        while True:
            cmd = input()
            self.process_cmd(cmd)

def test():
    host = input('enter host name\n')
    ftp_client = FtpClient(host)
    ftp_client.run()

test()
