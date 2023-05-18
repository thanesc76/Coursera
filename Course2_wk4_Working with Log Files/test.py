import sys
import os
import re

error = "CRON ERROR Failed to start"
log = "July 31 00:33:31 mycomputername system[25588]: ERROR Out of yellow ink, specifically, even though you want grayscale"
log = "July 31 04:11:32 mycomputername CRON[51253]: ERROR: Failed to start CRON job due to script syntax error. Inform the CRON job owner!"
error_patterns = ["error"]
for i in range(len(error.split(' '))):
  error_patterns.append(r"{}".format(error.split(' ')[i].lower()))

all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns)
