import json
import os

def create_multilingual_jsonl(folder_path, output_file):
    print("Starting the multilingual data extraction...\n")
    
    # 1. Define the source file (English)
    source_file_path = os.path.join(folder_path, "en-US.json")
    
    if not os.path.exists(source_file_path):
        print(f"ERROR: Source file '{source_file_path}' not found! Check your folder name.")
        return

    # Read the English source data
    with open(source_file_path, 'r', encoding='utf-8') as f_en:
        en_data = json.load(f_en)

    # 2. A dictionary to map language codes to readable names for the AI's prompt
    language_map = {
        "tr-TR": "Turkish",
        "de-DE": "German",
        "fr-FR": "French",
        "es-ES": "Spanish"
    }

    total_lines = 0

    # 3. Open the output file in 'write' mode ('w')
    with open(output_file, 'w', encoding='utf-8') as f_out:
        
        # 4. Loop through every file in our folder
        for file_name in os.listdir(folder_path):
            # Skip the English file and any non-JSON files
            if file_name == "en-US.json" or not file_name.endswith(".json"):
                continue
                
            # Extract the language code (e.g., "tr-TR.json" -> "tr-TR" using slicing [:-5])
            lang_code = file_name[:-5] 
            target_language_name = language_map.get(lang_code, lang_code)
            target_file_path = os.path.join(folder_path, file_name)
            
            # Open the target language file
            with open(target_file_path, 'r', encoding='utf-8') as f_target:
                target_data = json.load(f_target)
                
                matched_lines = 0
                
                # 5. Match keys between English and Target language (QA check)
                for key, en_text in en_data.items():
                    # If the key exists in the target file AND it's not empty
                    if key in target_data and str(target_data[key]).strip() != "":
                        target_text = target_data[key]
                        
                        # 6. DYNAMIC SYSTEM PROMPT: Tell the AI exactly what language to translate into
                        system_message = f"You are a professional game localization expert. Translate the English game texts into {target_language_name} ({lang_code}), keeping the context and game terminology accurate."
                        
                        # Format data into the standard LLM Chat format
                        formatted_data = {
                            "messages": [
                                {"role": "system", "content": system_message},
                                {"role": "user", "content": en_text},
                                {"role": "assistant", "content": target_text}
                            ]
                        }
                        
                        # Convert the Python dictionary into a JSONL string and write it to the file
                        json_line = json.dumps(formatted_data, ensure_ascii=False)
                        f_out.write(json_line + "\n")
                        
                        matched_lines += 1
                        total_lines += 1
                
                print(f"[{target_language_name}] successfully processed: {matched_lines} lines added.")

    print("-" * 40)
    print(f"Process Complete! A total of {total_lines} multilingual training lines saved to '{output_file}'.")

# 7. Run the function
create_multilingual_jsonl("game_loc_files", "multilingual_game_dataset.jsonl")