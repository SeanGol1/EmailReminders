import sys
import time

from Alarm import QtCore, QtGui
from espeak import espeask
from time import strftime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
      def _fromUtf8(s):
          return s
        