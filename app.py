import streamlit as st
import requests
import json

# Set your API key and deployment URL
API_KEY = "2W_bdZkTMAK6DS12sof3jMX8YJwxNSZtfziXEriF7ZYp"
DEPLOYMENT_URL = "https://private.au-syd.ml.cloud.ibm.com/ml/v4/deployments/e5835db5-0e79-4289-a316-c17a7715315b/predictions?version=2021-05-01"

st.title("NSAP Scheme Predictor")
st.markdown("Enter complete demographic and socio-economic details below:")

# Input fields
finyear = st.selectbox("Financial Year", ["2025-2026", "2024-2025", "2023-2024"])
lgdstatecode = st.number_input("State Code (lgdstatecode)", min_value=1)
statename = st.text_input("State Name", value="JAMMU AND KASHMIR")
lgddistrictcode = st.number_input("District Code (lgddistrictcode)", min_value=1)
districtname = st.text_input("District Name", value="ANANTNAG")

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

if st.button("Predict NSAP Scheme"):
    with st.spinner("Contacting the model API..."):
        # Get access token
        token_response = requests.post(
            'https://iam.cloud.ibm.com/identity/token',
            data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
        )

        if token_response.status_code != 200:
            st.error("Failed to get access token from IBM Cloud.")
        else:
            try:
                mltoken = token_response.json()["access_token"]

                headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

                # Construct input
                fields = [
                    "finyear", "lgdstatecode", "statename", "lgddistrictcode", "districtname",
                    "totalbeneficiaries", "totalmale", "totalfemale", "totaltransgender",
                    "totalsc", "totalst", "totalgen", "totalobc", "totalaadhaar", "totalmpbilenumber"
                ]

                values = [[
                    finyear, lgdstatecode, statename, lgddistrictcode, districtname,
                    totalbeneficiaries, totalmale, totalfemale, totaltransgender,
                    totalsc, totalst, totalgen, totalobc, totalaadhaar, totalmpbilenumber
                ]]

                payload = {
                    "input_data": [
                        {
                            "fields": fields,
                            "values": values
                        }
                    ]
                }

                response = requests.post(DEPLOYMENT_URL, json=payload, headers=headers)

                if response.status_code == 200:
                    prediction = response.json()["predictions"][0]["values"][0][0]
                    st.success(f"✅ Predicted NSAP Scheme: **{prediction}**")
                else:
                    st.error(f"❌ API Error: {response.status_code} — {response.text}")

            except Exception as e:
                st.error(f"Unexpected error occurred: {e}")

