import csv
import json
import os

def csv_to_jsonl(input_csv_path, output_jsonl_path):
    """
    Convert the first column of a CSV file to a JSONL file with 'question' field.
    
    Args:
        input_csv_path (str): Path to the input CSV file
        output_jsonl_path (str): Path to the output JSONL file
    """
    # Check if input file exists
    if not os.path.exists(input_csv_path):
        print(f"Error: Input file '{input_csv_path}' does not exist.")
        return False
    
    try:
        with open(input_csv_path, 'r', encoding='utf-8') as csv_file, \
             open(output_jsonl_path, 'w', encoding='utf-8') as jsonl_file:
            
            # Create a CSV reader
            csv_reader = csv.reader(csv_file)
            
            # Process each row
            for i, row in enumerate(csv_reader):
                if i==0:
                    continue  # Skip the header row
                if row and len(row) > 0:  # Check if row exists and has at least one column
                    # Create a dictionary with 'question' field containing the first column value
                    json_obj = {"question": row[0]}
                    
                    # Write the JSON object as a line in the JSONL file
                    jsonl_file.write(json.dumps(json_obj, ensure_ascii=False) + '\n')
        
        print(f"Conversion completed. Output saved to '{output_jsonl_path}'")
        return True
    
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False

def filter_and_index_jsonl(input_jsonl_path, output_jsonl_path):
    """
    读取JSONL文件，过滤特定值，添加编号，并确保idx字段排在第一位
    
    Args:
        input_jsonl_path (str): 输入JSONL文件路径
        output_jsonl_path (str): 输出JSONL文件路径
    """
    # 要过滤的值列表
    filter_values = ['数学（多要求，多步骤）', '文字（文字游戏，多要求文本，严格格式，韵母）']
    
    # 检查输入文件是否存在
    if not os.path.exists(input_jsonl_path):
        print(f"错误: 输入文件 '{input_jsonl_path}' 不存在。")
        return False
    
    try:
        # 读取输入文件，过滤数据
        filtered_data = []
        filtered_out_data = []
        
        with open(input_jsonl_path, 'r', encoding='utf-8') as jsonl_file:
            for line in jsonl_file:
                if line.strip():  # 确保行不为空
                    item = json.loads(line)
                    question = item.get('question', '')
                    
                    # 检查是否需要过滤
                    if question in filter_values or not question:
                        filtered_out_data.append(item)
                    else:
                        filtered_data.append(item)
        
        # 打印被过滤掉的数据
        print(f"以下 {len(filtered_out_data)} 条数据被过滤掉:")
        for item in filtered_out_data:
            print(f"  - {item}")
        
        # 添加编号并重新排列字段
        indexed_data = []
        for idx, item in enumerate(filtered_data, 1):
            # 创建新的字典，确保idx字段在第一位
            new_item = {"idx": idx}
            # 将其他字段添加到新字典中
            for key, value in item.items():
                new_item[key] = value
            
            indexed_data.append(new_item)
        
        # 写入输出文件
        with open(output_jsonl_path, 'w', encoding='utf-8') as output_file:
            for item in indexed_data:
                output_file.write(json.dumps(item, ensure_ascii=False) + '\n')
        
        print(f"处理完成。过滤和编号后的数据已保存到 '{output_jsonl_path}'")
        print(f"原始数据: {len(filtered_data) + len(filtered_out_data)} 条")
        print(f"过滤后数据: {len(filtered_data)} 条")
        return True
    
    except Exception as e:
        print(f"处理过程中出错: {str(e)}")
        return False

if __name__ == "__main__":
    # Input and output file paths
    input_file = "/map-vepfs/yiming/KOR-Bench/data/lookfowarding/前瞻bench - Sheet1.csv"
    output_file = "/map-vepfs/yiming/KOR-Bench/data/lookfowarding/questions.jsonl"
    
    # Execute the conversion
    csv_to_jsonl(input_file, output_file)
    # 执行过滤和编号
    filter_and_index_jsonl(output_file, output_file.replace('questions','lookforward'))