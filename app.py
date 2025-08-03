import streamlit as st
import requests
import json

# App Title
st.title("NSAP Scheme Predictor")
st.markdown("Enter the complete demographic and socio-economic details below:")

# Input Fields
finyear = st.selectbox("Financial Year", ["2025-2026", "2024-2025", "2023-2024"])
lgdstatecode = st.number_input("State Code (lgdstatecode)", min_value=1)
statename = st.text_input("State Name (statename)", value="JAMMU AND KASHMIR")
lgddistrictcode = st.number_input("District Code (lgddistrictcode)", min_value=1)
districtname = st.text_input("District Name (districtname)", value="ANANTNAG")

totalbeneficiaries = st.number_input("Total Beneficiaries", min_value=0)
totalmale = st.number_input("Total Male", min_value=0)
totalfemale = st.number_input("Total Female", min_value=0)
totaltransgender = st.number_input("Total Transgender", min_value=0)

totalsc = st.number_input("Total SC", min_value=0)
totalst = st.number_input("Total ST", min_value=0)
totalgen = st.number_input("Total General", min_value=0)
totalobc = st.number_input("Total OBC", min_value=0)

totalaadhaar = st.number_input("Total Aadhaar Linked", min_value=0)
totalmpbilenumber = st.number_input("Total Mobile Numbers", min_value=0)

# Predict Button
if st.button("Predict NSAP Scheme"):
    # Construct payload
    payload = {
        "input_data": [{
            "fields": [
                "finyear", "lgdstatecode", "statename", "lgddistrictcode", "districtname",
                "totalbeneficiaries", "totalmale", "totalfemale", "totaltransgender",
                "totalsc", "totalst", "totalgen", "totalobc", "totalaadhaar", "totalmpbilenumber"
            ],
            "values": [[
                finyear, lgdstatecode, statename, lgddistrictcode, districtname,
                totalbeneficiaries, totalmale, totalfemale, totaltransgender,
                totalsc, totalst, totalgen, totalobc, totalaadhaar, totalmpbilenumber
            ]]
        }]
    }

    # API call
    url = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/e5835db5-0e79-4289-a316-c17a7715315b/predictions?version=2021-05-01"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer ApiKey-e6233110-f3a2-4740-bbad-af86dafda5b9"
    }

    response = requests.post(url, headers=headers, json=payload)

    # Result display
    if response.status_code == 200:
        prediction = response.json()["predictions"][0]["values"][0][0]
        st.success(f"✅ Predicted NSAP Scheme: **{prediction}**")
    else:
        st.error(f"❌ API Error: {response.status_code}\n{response.text}")
