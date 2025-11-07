from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re
import hashlib



def find_launch_date():
    url = "https://www.jpl.nasa.gov/missions/voyager-1/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    launch_label = soup.find("p", class_='label', string='Launch Date')

    if launch_label:
        launch_date_elem = launch_label.find_next_sibling('p')
        if launch_date_elem:
            launch_date = launch_date_elem.get_text()

            month_mapper = {
                'Jan': '01',
                'Feb': '02',
                'Mar': '03',
                'Apr': '04',
                'May': '05',
                'Jun': '06',
                'Jul': '07',
                'Aug': '08',
                'Sept': '09',
                'Oct': '10',
                'Nov': '11',
                'Dec': '12'
            }
            parts = launch_date.replace(',', '').replace('.', '').split()
            month, day, year = parts
            month = month_mapper.get(month)
            day = day.zfill(2)
            return f"{year}{month}{day}"

    return None


def find_rfc1149_date():
    url = "https://datatracker.ietf.org/doc/html/rfc1149"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    pre_content = soup.find('pre')
    if pre_content:
        text = pre_content.get_text()
        pattern = r"\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}"
        date_pattern = re.compile(pattern, re.IGNORECASE)
        match = date_pattern.search(text)
        if match:
            date = match.group()
            date_obj = datetime.strptime(date, "%d %B %Y")
            formatted_date = date_obj.strftime("%Y%m%d")
            return formatted_date


def get_brain_codepoint_anchor():
    url = "https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt"
    response = requests.get(url)
    response.raise_for_status()
    for line in response.text.splitlines():
        if 'BRAIN' in line:
            return line.split(';')[0]
    return None


def get_genesis_date_simple():
    url = "https://blockstream.info/api/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"

    response = requests.get(url)
    data = response.json()
    timestamp = data['timestamp']

    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime('%Y%m%d')


def find_kr2_isbn10():
    url = "https://s3-us-west-2.amazonaws.com/belllabs-microsite-dritchie/cbook/index.html"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for text in soup.stripped_strings:
        if 'ISBN' in text:
            return text.strip().split()[1].replace('-', '')
    return None


flag = f'{find_launch_date()}-{find_rfc1149_date()}-{get_brain_codepoint_anchor()}-{get_genesis_date_simple()}-{find_kr2_isbn10()}'
flag_encode = flag.encode('utf-8')
hash256 = hashlib.sha256()
hash256.update(flag_encode)
print(hash256.hexdigest())