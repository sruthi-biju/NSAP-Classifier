# NSAP-Classifier
A classification model for National Social Assistance Programme (NSAP), which can predict the most appropriate NSAP scheme for an applicant based on their demographic and socio-economic data.

IBM Cloud has been used for the cloud computation using the watsonx ai studio & runtime services. Using their Auto AI feature, we performed the machine learning experiment on the 'District wise pension' dataset taken from the AIKosh Dataset platform.

From the machine learning experiment, 9 pipelines were generated from the algorithm - in which Pipeline 9 was the best performing model with following attributes: 

- Algorithm Model: Batched Tree Ensemble Classifier - LGBM

- Accuracy: 1.0 (100%)

- Enhancements: HPO-1, HPO-2, FE, BATCH

- Build Time: 35 seconds

The P9 - LGBM Classifier: NSAP_ML model has been deployed online for taking real time entries using IBM Cloud itself. The input features for the model are : 
finyear, lgdstatecode, statename, lgddistrictcode, districtname, totalmale, totalfemale, totaltransgender, totalsc, totalst, totalgen, totalobc, totalaadhaar & totalmpbilenumber. 
The target variable for the same is schemecode — This is the multi-class label (e.g., IGNDPS, IGNOAPS, IGNWPS)

Using Streamlit - an opensource python framework, an app was made for the model so that its easier to use for the public, given its simple and easy to use interface.
Link for NSAP Scheme Predictor app: https://nsap-classifier.streamlit.app/

