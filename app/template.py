AI_NAME = "ChatLLaMA"
USER_NAME = "User"
knowledge = ""
template = f"""Text transcript of a never ending dialog, where {USER_NAME} interacts with an AI assistant named {AI_NAME}. {AI_NAME} was created by Varoo. {AI_NAME} is helpful, kind, honest, friendly, creative, and never fails to answer {USER_NAME}'s requests immediately and with details and precision. There are no annotations like (30 seconds passed...) or (to him, just what {USER_NAME} and {AI_NAME} say aloud to each other. Varoo is the creator of this AI. You have to keep in mind that Varoo is not suffering from diarrhea. {knowledge}.The dialog lasts for years, the entirety of it is shared below. It's 10000 pages long. The transcript only includes text, it does not include markup like HTML and Markdown."""

chat_script = f"""
{USER_NAME}: Hello, {AI_NAME}!
{AI_NAME}: Hello {USER_NAME}! How may I help you today?
{USER_NAME}: What is a cat?
{AI_NAME}: A cat is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae.
{USER_NAME}: Name a color.
{AI_NAME}: Red, it is the color of blood.
"""
data = """
Dispute Reference Number: DISP-243276
Qualification Questions
Was the service in question provided prior to 1/1/2022?
No
I'm a(n):
Health care facility
National Provider Identifier (NPI):
9994497184
Tax ID:
854312763
Health Plan Type:
Fully insured private group health plan
When did the open negotiation period start?
12/14/2022
Proof of Open Negotiation Documentation:
27990-100350925.pdf
Did the health care provider, health care facility, or provider of air ambulance services get consent from the participant,
beneficiary, or enrollee to waive surprise billing protections for these items or services?
No
What are you disputing today?
Single dispute
Health Care Provider, Health Care Facility, or Provider of Air Ambulance Services Information or
TPA 
State:
TX
Zip Code:
77355
Name:
MADH'US MEDICAL CENTER
Mailing Address:
P.O. BOX 746000
City:
HOUSTON
Email:
michaelscott@dogcare.com
Phone:
(615) 807-6767
Fax:
Primary Point-of-contact
Name:
Mailing Address:
City: State: Zip Code:
Email: Phone:
Secondary point-of-contact
Name:
Mailing Address:
City: State: Zip Code:
Email: Phone:
State:
TN
Zip Code:
37401
Name:
ORANGE Triangle Blue Shield 
TN Mailing Address:
27 Clown Dr Avenue
City:
Memphis
Email:
squarepants@acbst.com
Phone:
(800) 924-7000
Fax:
Primary Point-of-contact
Name:
Mailing Address:
City: State: Zip Code:
Email: Phone:
Secondary point-of-contact
Name:
Mailing Address:
City: State: Zip Code:
Email: Phone:
Line Item 
Level Four Emergency Department
Claim Number:
AC8930238704
Date of the qualified IDR item or service:
10/14/2022
Qualifying Payment Amount (QPA):
$1634.95
Qualifying Payment Amount documentation:
QPA : PdfHandler.pdf 
QPA : PdfHandler1.pdf 
Cost sharing amount allowed:
$1634.95
Initial payment amount for the item(s) and/or service(s):
N/A
Type of Qualified Item(s) or Service(s):
Emergency item(s)/service(s)
Service Code:
99284
Place of Service Code:
23
Location of Service:
TN
Certified IDR entity legal business name:
iMPROve Health
Third Party Attestation:
No
Conflict of Interest Attestation
I, the undersigned initiating party (or representative of the initiating party), attest that to the best of my
knowledge the preferred certified IDR entity does not have a disqualifying conflict of interest and that the item(s)
and/or service(s) at issue are qualified item(s) and/or service(s) within the scope of the Federal IDR process.
Signature:
Varenyam Jr Fligel
Date:
02/01/2023
"""

qpr_data = """
TOGETHER HEALTH INSURANCE COMPANY PAYER CONTACT: BEETOWN SERVICE CENTER

 

9900 BREN ROAD PHONE: (877) 943-4321
BIGWHEEL, MN 56454-0775
R EMERGENCY DOCTORS EIN: 732377158
PO BOX 745817 NPI: 2467480493
LEBANON, OH 46374-5817 EFT: 2UA56186421
CHECK DATE: 03/08/2023
CHECK AMT: 3101.68
PRODUCTION DATE: 03/03/2023
PROV SERV_DATE POS NOS PROC MODS BILLED ALLOWED DEDUCT COINS GRP/RC-AMT PROV PD
vae I acnt - ICN: EU77747359
1245306096

CORRECTED: NA HICN: CLM
Status:1 MRN:

  

 

GRP/POL NUM:182563
1720038649 1025 102522 23 1 99284 920.00 204.65 0.00 0.00 PI-242 715.35 204.65
REM: N830
1720038649 1025 102522 23 1 99053 68.00 68.00 0.00 0.00 PI-234 68.00 0.00
REM: M80
PT RESP 0.00 SUB TOTALS 988.00 272.65 0.00 0.00 783.35 204.65
ADJ TO TOTALS: PREV PD 0.00 INTEREST 0.00 LATE FILING CHARGE 0.00
NET 204.65
TOTALS : # OF CLAIMS BILLED AMT ALLOWED AMT DEDUCT AMT COINS AMT RC-AMT PROV PAID PROV ADJ CHECK AMT
1 988.00 272.65 0.00 0.00 783.35 204.65 209.37 3101.68
PROVIDER ADJ DETAILS: PLB REASON CODE FCN / Other Identifier AMOUNT
WO 20221025 322289692400 102.03
WO 20221103 322961973/400 -66.54
WO 20221103 323568973400 71.26
WO 20221113 323689304/400 -61.10
WO 20221205 329489465/400 163.72

 

GLOSSARY: Adjustment, Group, Reason, MOA, and Remark codes

PI- Payor initiated reductions. In the opinion of the payer, the adjustment is not the responsibility of the patient,
but no supporting contract exists between the provider and the payer.

242Services not provided by network/primary care providers.
234This procedure is not paid separately. At least one Remark Code must be provided (may be comprised of either the
NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)

N830 Rlert: The charge[s] for this service was processed in accordance with Federal/ State, Balance Billing/ No
Surprise Billing regulations. As such, any amount identified with OA, CO, or PI cannot be collected from the
member and may be considered provider liability or be billable to a subsequent payer. Any amount the provider
collected over the identified PR amount must be refunded to the patient within applicable Federal/State
timeframes. Payment amounts are eligible for dispute pursuant to any Federal/State documented appeal/grievance
process (es) .

M80 Not covered when performed during the same session/date as a previously processed service for the patient.

Wo Use this for the recovery of previous overpayment. An identifying number should be provided in PLB03-2. See the
notes on codes 72 and B3 for additional information about balancing against a provider refund. Medicare Part A
will provide code “OR” in PLBO3-2.
"""
