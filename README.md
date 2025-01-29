# 📌 Stibo-Hackathon: Automated Reset for Oracle 19c VM Deployment

## 🔄 Overview
In **multi-tenant SaaS platforms**, ensuring **isolated environments** for individual tenants is crucial. These environments often need to be **reset** to a known baseline for **development, testing, or compliance**.

This project **automates** the reset process for an **Oracle 19c tenant database**, offering a **scalable** and **efficient** solution for environment refreshes using **Oracle Data Pump** (`impdp`) and **Azure Blob Storage**.

✅ **Drop the existing tenant database.**  
✅ **Import a fresh database** using a Data Pump (`.dmp`) file stored in **Azure Blob Storage**.  
✅ **Minimize downtime** and ensure **reliable database refreshes**.  
✅ **Send an email notification** after a **successful or failed reset**.

---

## 🛠 Prerequisites
Ensure the following are installed and configured before running the scripts:

✅ **Oracle Database 19c** with Data Pump utilities (`expdp`, `impdp`).  
✅ **Azure CLI (`az`)** installed and authenticated.  
✅ **An Azure Storage Account** and **Blob Container**.  
✅ **Python 3.12** with `smtplib` and `email` libraries for notifications.

---

## 📂 Code Repository
- 📁 **`scripts/`** → **Automation scripts** (Python, Bash, SQL)  
- 📁 **`config/`** → **Configuration files** (Database credentials, Azure settings)  
- 📁 **`sql/`** → **SQL scripts** for table creation, privilege grants, and directory setup  
- 📄 **`README.md`** → **Setup instructions**

---

## ⚙️ Setup Instructions

### 1️⃣ Database Table Creation
Ensure the **STUDENTS** table exists before running `expdp`.  
📌 **SQL commands are available in the `All_Files/` folder.**

---

### 2️⃣ Grant Necessary Privileges
Oracle requires specific privileges for **Data Pump** operations.  
📌 **Privilege grant commands are in the `All_Files/` folder.**

---

### 3️⃣ Create an Oracle Directory Object
Run the following SQL command:

``sql
CREATE OR REPLACE DIRECTORY DATA_PUMP_DIR AS 'Dir_Path';


## 🔄 Database Drop and Import Process

### 🚀 Export and Upload the Database (`expdp`)
- Run the **export command** provided in the `All_File` folder.

📌 **Uploads the dump file to Azure Blob Storage** using the command:

``sh
az storage blob upload --container-name <container_name> --file <dmp_file>


### 📥 Database Reset Process (`impdp`)
1️⃣ **Run the automation script** to drop the existing table.  
2️⃣ **Run the automation script** to restore the database from **Azure Blob Storage**.

📌 **Ensures a fresh database reset.**

---

### 📧 Email Notification Integration
After the reset process, an **email notification** is sent to **administrators** regarding the **status of the reset**.

- ✅ **Success Email:** Sent when the reset is **completed successfully**.
- ✅ **Failure Email:** Sent if any step **fails** (download, drop, or import).


### 📧 Contact
For any questions or issues, contact me:  
📧 **Email:** [vartikapathak74@gmail.com](mailto:vartikapathak74@gmail.com)


