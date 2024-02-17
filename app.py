# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_MYVYklFd9ee3OzHl-mhD2slytO5ak5p
"""

import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

header = st.container()
application = st.container()

# load dataset
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/kewchi/capstone/main/dataset.csv'
    data = pd.read_csv(url)
    return data

# loading the trained model
pickle_in = open('rf.pkl', 'rb')
model = pickle.load(pickle_in)

# defining the function to give the output using the user input
def output(diagnosis, prescription):
  translated_input = np.empty(2)
  data = load_data()

 # Fit the LabelEncoder on the labels in the diagnosis column
  led = LabelEncoder()
  led.fit(data['OpticalDiagnosisCode'])

 # Fit the LabelEncoder on the labels in the prescription column
  lep = LabelEncoder()
  lep.fit(data['ServiceItemName'])

 # Encode input for diagnosis
  transdiagnosis = led.transform([diagnosis]) 

 # Encode input for prescription
  transprescription = lep.transform([prescription]) 

  destination_array[0] = transdiagnosis 
  destination_array[1] = transprescription
    
  #predicting if it is voided or not
  output = model.predict([[destination_array]])

  if output == 0:
      res = 'Not Voided'
  else:
      res = 'Voided'
  return res

with header:
    st.title('Diagnosis-based prescription error detection')

with application:
    st.header('Instructions')
    st.text('Choose a diagnosis from the drop down list and enter the values accordingly')
    st.text('--------------------------------------------------------------------------')
    sel_col, disp_col = st.columns(2)

    diagnosis = sel_col.selectbox('Please Select a Diagnosis',
                                       options=['HYPERMETROPIA', 'HYPOTONY', 'ACCOMODATION AND CONVERGENCE ABNORMALITIES','DIABETIC MACULAR ISCHAEMIA-DIABETIC MACULOPATHY', 'DISCIFORM KERATITIS-HERPES SIMPLEX KERATITIS',
                                                'LATENT ANGLE-CLOSURE GLAUCOMA-PRIMARY ANGLE-CLOSURE GLAUCOMA', 'LID LESION', 'FUCHS ENDOTHELIAL DYSTROPHY-CORNEAL DYSTROPHIES', 'GLAUCOMA SUSPECT',
                                                'CHRONIC ANGLE-CLOSURE GLAUCOMA-PRIMARY ANGLE-CLOSURE GLAUCOMA','CONGENITAL GLAUCOMA', 'ACQUIRED NASOLACRIMAL DUCT OBSTRUCTION-LACRIMAL OBSTRUCTION','EPIBLEPHARON-MISCELLANEOUS CONGENITAL DISORDERS', 'ESOTROPIA', 'ACTIVE TED-THYROID EYE DISEASE',
                                                'ACUTE ALLERGIC OEDEMA-ALLERGIC DISORDERS', 'ADENOVIRAL KERATOCONJUCTIVITIS-VIRAL CONJUNCTIVITIS', 'BAND KERATOPATHY-CORNEAL DEGENERATIONS' 'BLUNT TRAUMA-GLOBE TRAUMA', 'CENTRAL RETINAL ARTERY OCCLUSION-RETINAL ARTERY OCCLUSION',
                                                'INFLAMMATORY GLAUCOMA' ,'IOL OPACIFICATION' ,'CORNEA HAZE', 'DELLEN-PERIPHERAL CORNEAL DISORDERS', 'EXUDATIVE MYOPIC MACULOPATHY-MYOPIC MACULOPATHY',
                                                'EXTERNAL HORDEOLUM-BENIGN NODULES AND CYSTS' ,'ENDOPHTHALMITIS', 'FILAMENTARY KERATITIS' ,'HEMIFACIAL SPASM', 'IDIOPATHIC MACULAR HOLE', 'HEMIRETINAL VEIN OCCLUSION-RETINAL VEIN OCCLUSION', 'MACULAR HOLE',
                                                'NYSTAGMUS', 'HERPES SIMPLEX CONJUNCTIVITIS-VIRAL CONJUNCTIVITIS', 'HETEROPHORIA'])

    prescription = sel_col.selectbox('Please Select a Medication to Prescribe',
                                       options=['FUCITHALMIC 10mg/g', 'NEVANAC (Nepafenac 0.1%)', 'PATADAY (Olopatadine HCL 0.2%)', 'TIMOLOL-POS 0.5%', 'CUSIVIRAL', 'VITAMODE ASTA I - CARE CAPSULE', 'HIALID 0.1%', 'OPTIVE FUSION MD 5ML',
                                                'OPTIVE FUSION MD 10ML', 'SYSTANE LID CARE WIPE', 'ARCOXIA 50MG', 'ZYMAXID 0.5%', 'DUOTRAV (BAK FREE) (Travoprost 40mcg + Timolol 5mg',
                                                'RELESTAT (Epinastine HCL 0.5mg)', 'FML 0.5%', 'VISMED MULTI 0.18%', 'CRAVIT 0.5%', 'PREDNISOLONE', 'SYSTANE HYDRATION (UNIT DOSE)', 'HYLO GEL',
                                                'BIO-VIZMAX CAPS', 'TAFLOTAN ', 'FML 0.1%','OPTIVE FUSION (UNIT DOSE) 30X0.4ML', 'TIMO-COMOD 0.5%', 'CETRIZINE 10mg',
                                                'TOBRADEX', 'AZYTER 15MG/G (0.25G 6S)', 'BIO-MARINE PLUS CAPSULES','SYSTANE ULTRA', 'PRED-FORTE (Prednisolone 1%)', 'LOTEMAX 0.5%',
                                                'SIMBRINZA (Brinzolamide 10mg + Brimonidine 2mg)', 'HYLO GEL 2mg/ml', 'AZOPT (Brinzolamide 10mg)', 'TIMOLOL-POS 0.3%', 'HYLO-COMOD 1mg/ml',
                                                'REFRESH LIQUIGEL', 'COMBIGAN', 'TRAVATAN (BAK FREE)', 'HIALID 0.5%','DUOTRAV', 'GANFORT', 'AZOPT', 'SIMBRINZA 5ML', 'VISMED MULTI',
                                                'DUOTRAV (BAK FREE)', 'DIAMOX 250mg', 'GENTAMICIN (0.3%) OINTMENT', 'TAPCOM-S (Tafluprost 15mcg + Timolol 5mg)', 'TIMOLOL-POS 0.10%', 'NEVANAC',
                                                'CUSIVIRAL / ACICLOVIR 30mg/g' 'HIALID 0.1', 'NEVANAC (Nepafenac 0.5%)', 'CATIONORM EYE DROP', 'CIPROFLOXACIN (800mg)', 'OMEPRAZOLE 20mg',
                                                'CIPROFLOXACIN (500mg)', 'PRED-FORTE', 'VIGAMOX (Moxiflocin HCL 0.5%)', 'CETRIZINE 5mg', 'FUCITHALMIC', 'ALPHAGAN P (0.15%)',
                                                'OPTIVE FUSION MD 50ML', 'VIDISIC GEL (Carbomer 2mg)', 'CUSIVIRAL / ACICLOVIR 10mg/g', 'CYCLOGYL', 'NEVANAC ', 'ARCOXIA 90MG'
                                                'SYSTANE COMPLETE 10ml', 'LATAPROST 0.005%', 'FUCITHALMIC 5mg/g', 'FML', 'HYLO-COMOD', 'LUMIGAN 0.01%'])

    # when 'Submit for checking' is clicked, make the prediction and store it
    if st.button("Submit for checking"):
        result = output(diagnosis, prescription)
        if result == 'Not Voided':
            st.success('Diagnosis and prescription is valid')
        else:
            st.error('Diagnosis and prescription is invalid')
