import streamlit as st
import json

def modify_json(data):
    if isinstance(data, dict):
        for key, value in list(data.items()):
            if key == "Vehicle Year >= 2023 & OEM" and value == "2023":
                data["Vehicle Year >= 2024 & OEM"] = "2024"
                del data[key]
            elif isinstance(value, (dict, list)):
                modify_json(value)
    elif isinstance(data, list):
        for item in data:
            modify_json(item)
    return data

def main():
    st.title("JSON Modifier")
    st.write("Upload a JSON file to modify specific values.")

    uploaded_file = st.file_uploader("Choose a JSON file", type="json")

    if uploaded_file is not None:
        data = json.load(uploaded_file)
        modified_data = modify_json(data)

        st.download_button(
            label="Download Modified JSON",
            data=json.dumps(modified_data, indent=4),
            file_name="modified_data.json",
            mime="application/json"
        )

if __name__ == "__main__":
    main()
