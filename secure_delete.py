import os
import logging

def secure_delete(file_path, iterations=3, block_size=4096):
    if not os.path.exists(file_path):
        logging.warning(f"File not found: {file_path}")
        return

    try:
        # Get the file size
        file_size = os.path.getsize(file_path)

        # Open the file in write mode
        with open(file_path, 'wb') as file:
            for i in range(iterations):
                file.seek(0)
                bytes_written = 0
                while bytes_written < file_size:
                    block = os.urandom(min(block_size, file_size - bytes_written))
                    file.write(block)
                    bytes_written += len(block)  # Corrected indentation
                logging.info(f"Overwrite iteration {i+1} completed.")

        # Delete the file permanently
        os.remove(file_path)
        logging.info(f"File securely deleted: {file_path}")
    except (IOError, OSError) as e:
        logging.error(f"Error occurred during secure deletion: {str(e)}")
