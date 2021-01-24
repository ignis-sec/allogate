import sys
import inspect

BULLET_FAIL    ="[\033[91m+\033[0m]"
BULLET_SUCCESS ="[\033[92m+\033[0m]"
BULLET_WARN    ="[\033[93m+\033[0m]"
BULLET_INFO    ="[\033[94m+\033[0m]"
BULLET_ALL     ="[\033[34m+\033[0m]"

LOGGING_FAIL=0
LOGGING_SUCC=1
LOGGING_WARN=2
LOGGING_INFO=3
LOGGING_ALL =4

VERBOSITY=0
CLAMP=100

SHOW_STACK_THRESHOLD=2
PADDING_CHAR="_"
PADDING_COLOR = "\033[90m"
STACK_COLOR = " \033[93m" 

def verbosity(v):
    VERBOSITY=v

def pprint(message,level=LOGGING_FAIL):
    if(VERBOSITY>=level):
        _pprint(message,level)

def _pprint(message, level=LOGGING_FAIL):
    if(VERBOSITY>=SHOW_STACK_THRESHOLD):
        frame = inspect.stack()[2]
        frame_info =  STACK_COLOR + "[" + frame.filename.split('\\')[-1].split('.')[0] + ":" + frame.function + "]\033[0m"
    else:
        frame_info=""

    if(len(message)>CLAMP):
        message = message[0:CLAMP-3] + "..."
    elif(VERBOSITY>=SHOW_STACK_THRESHOLD):
        message += PADDING_COLOR + PADDING_CHAR * (CLAMP-len(message)) + "\033[0m"
    
    
    if(level==LOGGING_FAIL):
        sys.stderr.write(f"{BULLET_FAIL} {message}{frame_info}\n")
    elif(level==LOGGING_SUCC):
        sys.stdout.write(f"{BULLET_SUCCESS} {message}{frame_info}\n")
    elif(level==LOGGING_WARN):
        sys.stdout.write(f"{BULLET_WARN} {message}{frame_info}\n")
    elif(level==LOGGING_INFO):
        sys.stdout.write(f"{BULLET_INFO} {message}{frame_info}\n")
    else:
        sys.stdout.write(f"{BULLET_ALL} {message}{frame_info}\n")