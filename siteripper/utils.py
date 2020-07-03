from datetime import datetime

def parse_date(date_str):
    date_time_obj = datetime.strptime(date_str, "%B %d, %Y")
    return(date_time_obj.strftime("%Y-%m-%d"))
    
