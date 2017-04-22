from .base import BaseWriter
from .writers import Stdout, Fstdout, Json, Fjson
from .team_writers import Gjson, Gstdout
import io

def get_writer(output_format='stdout', output_file=None):
    return globals()[output_format.capitalize()](output_file)
