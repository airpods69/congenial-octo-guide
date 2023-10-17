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
{USER_NAME}: Do you know about the medical field?
{AI_NAME}: Yes, I am aware of the medical field. What specifically would you like to know about it?
{USER_NAME}: """

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
