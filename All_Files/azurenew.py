from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import subprocess
import os

# Azure Blob Storage configuration
connection_string = "DefaultEndpointsProtocol=https;AccountName=dyno098;AccountKey=4Gu78KQDd5HTxFIaCXb7h5zgy4RFPRbFf4DifQ8yMAk4faciC7MEtxtNBmt5r9sM0uyiF7/+JRT8+AStTUFVSg==;EndpointSuffix=core.windows.net"
container_name = "stibo-123"
blob_name = "STUDENTS.dmp"
local_file_path = r'C:\app\admin\orcl\dpdump\STUDENTS.dmp'


# Step 1: Download the Data Pump file from Azure Blob Storage
def download_blob():
    # Connect to Azure Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Download the blob to a local file
    with open(local_file_path, "wb") as file:
        blob_data = blob_client.download_blob()
        file.write(blob_data.readall())
    print(f"Downloaded {blob_name} to {local_file_path}")


# Step 3: Import the Data Pump file using impdp
def import_data():
    try:
        # Run the impdp command to import the data
        command = f"impdp system/shubrat@ORCL DIRECTORY=DATA_PUMP_DIR DUMPFILE=STUDENTS.dmp LOGFILE=students_import.log"
        subprocess.run(command, shell=True, check=True)
        print("Import completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during import: {e}")

# Step 4: Execute the steps
def reset_database():
    download_blob()
    import_data()

# Run the automation
reset_database()
