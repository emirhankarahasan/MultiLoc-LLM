import json
import os
import polib

def create_po_to_jsonl(folder_path, output_file):
    print("Starting the PO data extraction process...\n")
    
    # Language mapping based on standard PO file naming (e.g., tr.po, de.po)
    language_map = {
        "tr": "Turkish",
        "de": "German"
    }

    total_lines = 0

    with open(output_file, 'w', encoding='utf-8') as f_out:
        
        for file_name in os.listdir(folder_path):
            # Process only .po files
            if not file_name.endswith(".po"):
                continue
                
            # Extract language code from filename (e.g., "tr.po" -> "tr" using slicing)
            lang_code = file_name[:-3] 
            target_language_name = language_map.get(lang_code, lang_code)
            target_file_path = os.path.join(folder_path, file_name)
            
            print(f"Reading [{target_language_name}] file: {file_name}...")
            
            try:
                # Parse the PO file using polib
                po_file = polib.pofile(target_file_path)
                matched_lines = 0
                
                # Loop through every translation entry in the PO file
                for entry in po_file:
                    en_text = entry.msgid.strip()
                    target_text = entry.msgstr.strip()
                    
                    # QA Check: Skip empty translations or PO metadata headers
                    if not en_text or not target_text:
                        continue
                        
                    # DYNAMIC SYSTEM PROMPT
                    system_message = f"You are a professional game localization expert. Translate the English game texts into {target_language_name} ({lang_code}), keeping the context and game terminology accurate."
                    
                    formatted_data = {
                        "messages": [
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": en_text},
                            {"role": "assistant", "content": target_text}
                        ]
                    }
                    
                    # Convert to JSONL format and write
                    json_line = json.dumps(formatted_data, ensure_ascii=False)
                    f_out.write(json_line + "\n")
                    
                    matched_lines += 1
                    total_lines += 1
                
                print(f"[{target_language_name}] successfully processed: {matched_lines} lines added.")
            except Exception as e:
                print(f"ERROR processing {file_name}: {e}")

    print("-" * 40)
    print(f"Process Complete! A total of {total_lines} training lines saved to '{output_file}'.")

# Run the engine
create_po_to_jsonl("game_loc_files", "multilingual_game_dataset.jsonl")