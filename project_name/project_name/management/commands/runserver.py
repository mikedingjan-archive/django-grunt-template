import os
import subprocess
import atexit
import signal
from optparse import make_option

from django.core.management.commands.runserver import Command as RunserverCommand


class Command(RunserverCommand):
    option_list = RunserverCommand.option_list + (
        make_option('--grunt', action='store_false', dest='grunt', help='Runs grunt watch at the same time as runserver'),
    )

    def inner_run(self, *args, **options):
        grunt = options.get('grunt')
        if grunt is not None:
            self.start_grunt()
        return super(Command, self).inner_run(*args, **options)

    def start_grunt(self):
        self.stdout.write('>>> Starting the grunt watch command')
        self.grunt_process = subprocess.Popen(
            ['grunt watch --gruntfile={{ project_name }}/static/Gruntfile.js --base=.'],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr,
        )

        self.stdout.write('>>> Grunt watch process on pid {0}'.format(self.grunt_process.pid))

        def kill_grunt_process(pid):
            self.stdout.write('>>> Closing grunt watch process')
            os.kill(pid, signal.SIGTERM)

        atexit.register(kill_grunt_process, self.grunt_process.pid)
