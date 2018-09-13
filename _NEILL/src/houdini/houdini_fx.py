from houdini_base import *

try:
    setHoudiniEnv()
    setRedshiftEnv()
    setMopsEnv()
    setQlibEnv()
    setGameDevEnv()

    cmd  = env['HB'] + '/houdinifx'
    la_utils.runCmd(cmd, env)
except:
    la_utils.print_error('Something broke.')