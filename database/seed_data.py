import sqlite3
import os

DB_PATH = os.path.join("database", "iffco.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ================= CLEAR MASTER DATA =================

cursor.execute("DELETE FROM districts")
cursor.execute("DELETE FROM sales")
cursor.execute("DELETE FROM fertilizers")
cursor.execute("DELETE FROM employees")
cursor.execute("DELETE FROM states")

# ================= EMPLOYEES =================

employees = [

(
"MGR001",
"Manager",
"manager@iffco.com",
"9999999999",
"01-01-1985",
"Male",
"IFFCO Head Office",
"Uttar Pradesh",
"Lucknow",
"Lucknow Branch",
"01-04-2012",
"Regional Sales Manager",
"Sales",
"Active",
"",
"admin123",
"manager"
),

(
"EMP001",
"Avinash Bhardwaj",
"avinash@iffco.com",
"9876543201",
"12-05-1998",
"Male",
"Bareilly",
"Uttar Pradesh",
"Bareilly",
"Bareilly Branch",
"15-07-2022",
"Senior Sales Executive",
"Sales",
"Active",
"",
"emp123",
"employee"
),

(
"EMP002",
"Aman Rajput",
"aman@iffco.com",
"9876543202",
"08-11-1999",
"Male",
"Kanpur",
"Uttar Pradesh",
"Kanpur",
"Kanpur Branch",
"10-02-2023",
"Area Sales Officer",
"Sales",
"Active",
"",
"emp123",
"employee"
),

(
"EMP003",
"Adarsh Bhardwaj",
"adarsh@iffco.com",
"9876543203",
"14-08-2004",
"Male",
"Bareilly",
"Uttar Pradesh",
"Bareilly",
"Bareilly Branch",
"01-06-2025",
"Sales Executive",
"Sales",
"Active",
"",
"emp123",
"employee"
),

(
"EMP004",
"Nanak Pandey",
"nanak@iffco.com",
"9876543204",
"15-03-1998",
"Male",
"Prayagraj",
"Uttar Pradesh",
"Prayagraj",
"Prayagraj Branch",
"22-09-2021",
"Field Sales Officer",
"Sales",
"Active",
"",
"emp123",
"employee"
),

(
"EMP005",
"Amul Singh",
"amul@iffco.com",
"9876543205",
"09-09-1997",
"Male",
"Jaipur",
"Rajasthan",
"Jaipur",
"Jaipur Branch",
"14-01-2020",
"Territory Sales Officer",
"Sales",
"Active",
"",
"emp123",
"employee"
),

(
"EMP006",
"Rahul Verma",
"rahul@iffco.com",
"9876543206",
"20-12-1996",
"Male",
"Lucknow",
"Uttar Pradesh",
"Lucknow",
"Lucknow Branch",
"10-11-2019",
"Agriculture Development Officer",
"Sales",
"Active",
"",
"emp123",
"employee"
)

]

cursor.executemany("""

INSERT INTO employees(

employee_id,
name,
email,
phone,
dob,
gender,
address,
state,
district,
branch,
joining_date,
designation,
department,
status,
photo,
password,
role
)
                                      
VALUES(
?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
)
                                      
""", employees)

# ================= STATES =================

states = [

"Uttar Pradesh",
"Bihar",
"Punjab",
"Haryana",
"Rajasthan",
"Madhya Pradesh",
"Gujarat",
"Maharashtra",
"Chhattisgarh",
"Jharkhand",
"West Bengal",
"Odisha",
"Assam",
"Tripura",
"Meghalaya",
"Nagaland",
"Manipur",
"Mizoram",
"Arunachal Pradesh",
"Sikkim",
"Uttarakhand",
"Himachal Pradesh",
"Jammu and Kashmir",
"Goa",
"Karnataka",
"Kerala",
"Tamil Nadu",
"Telangana",
"Andhra Pradesh"

]

for state in states:

    cursor.execute(
        "INSERT INTO states(state_name) VALUES(?)",
        (state,)
    )

# ================= DISTRICTS =================

district_data = {

    "Uttar Pradesh": ["Lucknow","Kanpur","Agra","Varanasi","Prayagraj"],
    "Bihar": ["Patna","Gaya","Muzaffarpur","Bhagalpur","Darbhanga"],
    "Punjab": ["Amritsar","Ludhiana","Patiala","Jalandhar","Bathinda"],
    "Haryana": ["Gurugram","Faridabad","Hisar","Panipat","Karnal"],
    "Rajasthan": ["Jaipur","Jodhpur","Kota","Ajmer","Udaipur"],
    "Madhya Pradesh": ["Bhopal","Indore","Gwalior","Jabalpur","Ujjain"],
    "Gujarat": ["Ahmedabad","Surat","Rajkot","Vadodara","Bhavnagar"],
    "Maharashtra": ["Mumbai","Pune","Nagpur","Nashik","Aurangabad"],
    "Chhattisgarh": ["Raipur","Bilaspur","Durg","Korba","Raigarh"],
    "Jharkhand": ["Ranchi","Jamshedpur","Dhanbad","Bokaro","Hazaribagh"],
    "West Bengal": ["Kolkata","Howrah","Asansol","Siliguri","Durgapur"],
    "Odisha": ["Bhubaneswar","Cuttack","Rourkela","Puri","Sambalpur"],
    "Assam": ["Guwahati","Silchar","Dibrugarh","Jorhat","Tezpur"],
    "Tripura": ["Agartala"],
    "Meghalaya": ["Shillong"],
    "Nagaland": ["Kohima"],
    "Manipur": ["Imphal"],
    "Mizoram": ["Aizawl"],
    "Arunachal Pradesh": ["Itanagar"],
    "Sikkim": ["Gangtok"],
    "Uttarakhand": ["Dehradun","Haridwar","Haldwani"],
    "Himachal Pradesh": ["Shimla","Mandi","Dharamshala"],
    "Jammu and Kashmir": ["Srinagar","Jammu"],
    "Goa": ["Panaji"],
    "Karnataka": ["Bengaluru","Mysuru","Hubballi","Belagavi"],
    "Kerala": ["Kochi","Thiruvananthapuram","Kozhikode"],
    "Tamil Nadu": ["Chennai","Coimbatore","Madurai","Salem"],
    "Telangana": ["Hyderabad","Warangal","Karimnagar"],
    "Andhra Pradesh": ["Vijayawada","Visakhapatnam","Guntur","Tirupati"]

}

for state_name, districts in district_data.items():

    cursor.execute(
        "SELECT id FROM states WHERE state_name=?",
        (state_name,)
    )

    state_id = cursor.fetchone()[0]

    for district in districts:

        cursor.execute(
            """
            INSERT INTO districts(state_id,district_name)
            VALUES(?,?)
            """,
            (state_id, district)
        )

# ================= FERTILIZERS =================

fertilizers = [

("IFFCO Urea",266),
("IFFCO DAP",1350),
("IFFCO NPK 10:26:26",1470),
("IFFCO NPK 20:20:0:13",1425),
("IFFCO MOP",1700),
("IFFCO Bio Fertilizer",450)

]

cursor.executemany("""

INSERT INTO fertilizers
(fertilizer_name,price_per_bag)

VALUES(?,?)

""", fertilizers)

conn.commit()
conn.close()

print("Master Data Inserted Successfully.")