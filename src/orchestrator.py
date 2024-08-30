# orchestrator.py

import subprocess
import signal
import sys
from config import get_logger

# Get the logger instance
logger = get_logger(__name__)

def start_deployment():
    logger.info("Starting deployment service...")
    deployment_process = subprocess.Popen(['python', 'src/deployment.py'])
    logger.info(f"Deployment service started with PID: {deployment_process.pid}")
    return deployment_process

def start_dashboard():
    logger.info("Starting dashboard service...")
    dashboard_process = subprocess.Popen(['python', 'src/dashboard.py'])
    logger.info(f"Dashboard service started with PID: {dashboard_process.pid}")
    return dashboard_process

def stop_process(process):
    if process:
        logger.info(f"Stopping process with PID: {process.pid}")
        process.terminate()

def main():
    deployment_process = None
    dashboard_process = None

    try:
        deployment_process = start_deployment()
        dashboard_process = start_dashboard()

        # Wait for the processes to complete
        deployment_process.wait()
        dashboard_process.wait()
    except KeyboardInterrupt:
        logger.info("Orchestrator interrupted. Shutting down services...")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
    finally:
        stop_process(deployment_process)
        stop_process(dashboard_process)
        logger.info("All services stopped.")

if __name__ == "__main__":
    main()
