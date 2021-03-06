from env.env_houdini import *

# enable_redshift()
# enable_plugins()

args = ' '.join(sys.argv[1:])

logging.info('Writing Environment to file...')
exe_file = write_exe('hython ' + args, LA_ENV)
logging.info('Done!')

logging.info('Starting Hython.')
logging.info('Using args : %s' % args)

run_exe(LA_ENV, exe_file)
