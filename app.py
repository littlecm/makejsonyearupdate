import streamlit as st
import json

def modify_json(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):
                modify_json(value)
            if key == "Vehicle Year >= 2023 & OEM" and value == "2023":
                data[key] = "Vehicle Year >= 2024 & OEM"
                data[key.replace("2023", "2024")] = "2024"
                del data[key]
    elif isinstance(data, list):
        for item in data:
            modify_json(item)
    return data

def main():
    st.title("JSON Modifier")
    st.write("Upload a JSON file and modify specific values.")

    uploaded_file = st.file_uploader("Choose a JSON file", type="json")

    if uploaded_file is not None:
        data = json.load(uploaded_file)
        st.write("Original JSON:")
        st.json(data)

        modified_data = modify_json(data)
        st.write("Modified JSON:")
        st.json(modified_data)

        st.download_button(
            label="Download Modified JSON",
            data=json.dumps(modified_data, indent=4),
            file_name="modified_data.json",
            mime="application/json"
        )

if __name__ == "__main__":
    main()
