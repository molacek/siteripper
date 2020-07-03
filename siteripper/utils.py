import subprocess
from datetime import datetime

def parse_date(date_str):
    date_time_obj = datetime.strptime(date_str, "%B %d, %Y")
    return(date_time_obj.strftime("%Y-%m-%d"))
    
def unzip(file_path):
    unpack_dir = file_path.parent / "tmp"    
    r = subprocess.run([
        "unzip",
        "-j",
        "-d",
        unpack_dir,
        file_path
    ])

    if r.returncode != 0:
        print(f"Error extracting {file_path}")
        return False

    # Delete file
    file_path.unlink()

    # Rename unpacked dir to original archive name
    unpack_dir.rename(file_path)

    return True

    
