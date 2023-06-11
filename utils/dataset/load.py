import requests
import zipfile
import os


def download_dataset(dataset_name: str) -> str:
    """
    Download a dataset based on its name.

    Args:
    dataset_name: str, the name of the dataset.

    Returns:
    str: The path to the downloaded dataset.

    Raises:
    ValueError: If the dataset_name is not supported.

    Example:
    download_dataset("social101")
    """

    if dataset_name == 'social101':
        # Define the URL and local file path for the ZIP file to download
        url = "https://storage.googleapis.com/ai2-mosaic-public/projects/social-chemistry/data/social-chem-101.zip"
        zip_file_path = "./social-chem-101.zip"

        # Send a download request
        response = requests.get(url)

        # Save the downloaded content to a local file
        with open(zip_file_path, "wb") as file:
            file.write(response.content)

        # Extract the ZIP file
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall("./")

        # Remove the original ZIP file
        os.remove(zip_file_path)

        # Return the path to the downloaded dataset
        return "./social-chem-101/"

    else:
        raise ValueError("Unsupported dataset_name. Please provide a valid dataset name.")



