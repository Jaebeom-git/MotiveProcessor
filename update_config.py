"""
MotiveProcessor Script

Author: Jaebeom Jo
Email: jojaebeom@gm.gist.ac.kr
"""

import json

def update_subject_num(subject_num):
    config_path = 'config.json'
    
    # JSON 파일 읽기
    with open(config_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
    
    # SUBJECT_NUM 업데이트
    config['SUBJECT_NUM'] = subject_num
    
    # JSON 파일 쓰기
    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4, ensure_ascii=False)
    
    print(f"SUBJECT_NUM updated to {subject_num} in {config_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python update_config.py <SUBJECT_NUM>")
    else:
        subject_num = int(sys.argv[1])
        update_subject_num(subject_num)
